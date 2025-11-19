# CONTENT-CREATOR

An AI-inspired helper for social media marketers. The toolkit builds a brand context profile from a website, blends in lightweight regional trend seeds, and generates concise post ideas that include headers, body copy, and clear calls to action. Exports are available for Excel, Word, and PowerPoint.

## Features
- Build a brand context profile from a provided website and inputs (category, tone, focus, audience).
- Generate 10–40 concise post ideas in seconds, following the requested tone and avoiding punctuation in headers/body lines.
- Pull region-aware trend seeds for local flair.
- Export to `.xlsx`, `.docx`, and `.pptx` for fast collaboration.

## Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the generator:
   ```bash
   python -m content_creator.app "Brand Name" "https://example.com" "Category" "Audience" "Tone" "Region" "Language" "Focus" --count 12
   ```
3. Outputs
   - Posts are printed to the console as `Post 1`, `Post 2`, etc.
   - Exported files are written to `./output/posts.xlsx`, `./output/posts.docx`, and `./output/posts.pptx` by default.

## Notes on Copy Rules
- Headers: 3–5 words, full sentences without internal punctuation.
- Body: 5–12 words, focuses on a customer problem and solution without punctuation.
- Call to Action: 2–6 words.

## Example
```bash
python -m content_creator.app "JESA Dairy" "https://jesadairy.com" "FMCG" "Gen Z 18-25" "Humorous" "Uganda" "English + Luganda" "Fresh milk"
```

## Testing
- The project uses `requirements.txt` for dependency installation. In network-restricted environments, installing packages such as `openpyxl` may fail due to proxy rules. Re-run `pip install -r requirements.txt` with the correct proxy configuration before executing the CLI example above.
