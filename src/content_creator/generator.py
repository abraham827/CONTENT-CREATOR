from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List

from .brand_profile import BrandContextProfile
from .trends import Trend, get_regional_trends


@dataclass
class PostIdea:
    header: str
    body: str
    cta: str


class ContentGenerator:
    def __init__(self, profile: BrandContextProfile):
        self.profile = profile
        self.trends = get_regional_trends(profile.region)

    def generate(self, count: int = 10) -> List[PostIdea]:
        ideas: List[PostIdea] = []
        for index in range(count):
            trend = self.trends[index % len(self.trends)]
            idea = self._build_post(trend, index)
            ideas.append(idea)
        return ideas

    def _build_post(self, trend: Trend, seed: int) -> PostIdea:
        random.seed(seed + len(self.profile.keywords))
        problem = self._select_problem()
        solution = self._select_solution()
        hook = self._header_hook(trend)
        header = f"{hook} {self.profile.brand_name}".lower()
        header = _truncate_words(header, 5)
        body = f"{problem} {solution} {trend.keyword}".lower()
        body = _truncate_words(body, 12)
        cta = self._cta()
        return PostIdea(header=header, body=body, cta=cta)

    def _header_hook(self, trend: Trend) -> str:
        tone = self.profile.tone.lower()
        if "humor" in tone:
            return f"{trend.keyword} meets"
        if "inspire" in tone:
            return f"rise with {trend.keyword}"
        if "inform" in tone:
            return f"learn from {trend.keyword}"
        return f"own the {trend.keyword}"

    def _select_problem(self) -> str:
        problems = [
            "stuck choosing whats next",
            "need a fast fix",
            "searching for local flavor",
            "want a budget friendly choice",
            "craving trusted quality",
            "need a fun break",
        ]
        return random.choice(problems)

    def _select_solution(self) -> str:
        solutions = [
            f"find it with {self.profile.brand_name}",
            f"refresh with {self.profile.focus}",
            f"make days easy with {self.profile.category}",
            f"enjoy comfort with {self.profile.brand_name}",
        ]
        return random.choice(solutions)

    def _cta(self) -> str:
        tones = [
            "try it today",
            "share the vibe",
            "join the moment",
            "see the freshness",
            "feel the spark",
        ]
        return random.choice(tones)


def _truncate_words(text: str, max_words: int) -> str:
    words = text.split()
    return " ".join(words[:max_words])
