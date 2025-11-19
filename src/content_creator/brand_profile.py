from __future__ import annotations

import re
import textwrap
import urllib.request
from dataclasses import dataclass, field
from html.parser import HTMLParser
from typing import List


class _MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title: str = ""
        self.meta_descriptions: List[str] = []
        self.text_chunks: List[str] = []
        self._capture_text = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "title":
            self._capture_text = True
        if tag == "meta" and attrs_dict.get("name", "").lower() == "description":
            content = attrs_dict.get("content", "")
            if content:
                self.meta_descriptions.append(content.strip())

    def handle_endtag(self, tag):
        if tag == "title":
            self._capture_text = False

    def handle_data(self, data):
        if self._capture_text:
            self.title += data.strip()
        elif data.strip():
            self.text_chunks.append(data.strip())


@dataclass
class BrandContextProfile:
    brand_name: str
    website: str
    category: str
    audience: str
    tone: str
    region: str
    language: str
    focus: str
    keywords: List[str] = field(default_factory=list)
    summary: str = ""


class BrandProfileBuilder:
    @staticmethod
    def from_website(brand_name: str, website: str, category: str, audience: str,
                     tone: str, region: str, language: str, focus: str) -> BrandContextProfile:
        parser = _MetaParser()
        extracted_text: str = ""
        try:
            with urllib.request.urlopen(website, timeout=8) as response:
                html = response.read().decode("utf-8", errors="ignore")
            parser.feed(html)
            combined_text = " ".join([parser.title] + parser.meta_descriptions + parser.text_chunks)
            extracted_text = _clean_text(combined_text)
        except Exception:
            extracted_text = f"{brand_name} {category} {focus}"

        keywords = _extract_keywords(extracted_text)
        summary = _build_summary(brand_name, category, focus, audience, tone, keywords)
        return BrandContextProfile(
            brand_name=brand_name,
            website=website,
            category=category,
            audience=audience,
            tone=tone,
            region=region,
            language=language,
            focus=focus,
            keywords=keywords,
            summary=summary,
        )


def _clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _extract_keywords(text: str, limit: int = 12) -> List[str]:
    words = re.findall(r"[A-Za-z]{4,}", text.lower())
    unique = []
    for word in words:
        if word not in unique:
            unique.append(word)
        if len(unique) >= limit:
            break
    return unique


def _build_summary(brand: str, category: str, focus: str, audience: str, tone: str, keywords: List[str]) -> str:
    keyword_part = ", ".join(keywords[:6]) if keywords else "brand values"
    summary = textwrap.dedent(
        f"""
        Brand: {brand}
        Category: {category}
        Focus: {focus}
        Audience: {audience}
        Tone: {tone}
        Keywords: {keyword_part}
        """
    ).strip()
    return summary
