from __future__ import annotations

import argparse
from pathlib import Path

from .brand_profile import BrandProfileBuilder
from .generator import ContentGenerator
from .exporters import export_to_excel, export_to_powerpoint, export_to_word


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate social content ideas quickly.")
    parser.add_argument("brand_name")
    parser.add_argument("website")
    parser.add_argument("category")
    parser.add_argument("audience")
    parser.add_argument("tone")
    parser.add_argument("region")
    parser.add_argument("language")
    parser.add_argument("focus")
    parser.add_argument("--count", type=int, default=10, help="Number of posts to generate")
    parser.add_argument("--outdir", default="output", help="Directory for exports")
    return parser.parse_args()


def build_and_generate(args: argparse.Namespace):
    profile = BrandProfileBuilder.from_website(
        brand_name=args.brand_name,
        website=args.website,
        category=args.category,
        audience=args.audience,
        tone=args.tone,
        region=args.region,
        language=args.language,
        focus=args.focus,
    )
    generator = ContentGenerator(profile)
    return generator.generate(args.count)


def print_posts(ideas) -> None:
    for idx, idea in enumerate(ideas, start=1):
        print(f"Post {idx}:")
        print(f"  Header: {idea.header}")
        print(f"  Body: {idea.body}")
        print(f"  Call to Action: {idea.cta}\n")


def main():
    args = parse_args()
    ideas = build_and_generate(args)
    print_posts(ideas)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    export_to_excel(ideas, outdir / "posts.xlsx")
    export_to_word(ideas, outdir / "posts.docx")
    export_to_powerpoint(ideas, outdir / "posts.pptx")


if __name__ == "__main__":
    main()
