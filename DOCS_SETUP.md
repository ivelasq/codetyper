# Documentation Website Setup

CodeTyper now has a professional documentation website built with [Great Docs](https://posit-dev.github.io/great-docs/)!

## What's Included

### 📚 User Guide

Three comprehensive guides in `user_guide/`:
- **Installation** - Setup instructions and troubleshooting
- **Quick Start** - 5-minute getting started guide
- **Script Format** - Complete reference for script configuration

### 📖 API Reference

Auto-generated API documentation from docstrings:
- `Config` - Main configuration class
- `CodeBlock` - Code block representation
- `CodeTyperError`, `ConfigurationError`, `ExecutionError` - Exception classes

### 🏠 Landing Page

Auto-generated from `README.md` with:
- Package description
- Installation instructions
- Quick examples
- Links to guides

### 🤖 AI-Friendly Files

Automatically generated:
- `llms.txt` - Concise package documentation for AI agents
- `llms-full.txt` - Complete documentation
- `skill.md` - Claude Code skill metadata

## Local Preview

View the documentation locally:

```bash
great-docs preview
```

Opens at http://localhost:3000

## Build Documentation

Generate the static site:

```bash
# Full rebuild
great-docs build

# Quick rebuild (skip API re-discovery)
great-docs build --no-refresh
```

Output: `great-docs/_site/`

## GitHub Pages Deployment

### Setup (One-time)

The GitHub Actions workflow is already configured at `.github/workflows/docs.yml`.

**To enable:**

1. **Push the workflow to GitHub:**
   ```bash
   git add .github/workflows/docs.yml great-docs.yml user_guide/
   git commit -m "Add documentation site"
   git push
   ```

2. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Set Source to "GitHub Actions"

3. **Trigger deployment:**
   - Push to `main` branch
   - Site will be live at: `https://[username].github.io/codetyper/`

### Automatic Updates

The workflow automatically:
- ✅ Builds docs on every push to `main`
- ✅ Deploys to GitHub Pages
- ✅ Creates preview deployments for PRs

## Configuration

Edit `great-docs.yml` to customize:

```yaml
# Author info
authors:
  - name: Your Name
    role: Author

# API organization
reference:
  - title: Configuration
    contents:
      - Config
      - CodeBlock

# Site settings
# site:
#   theme: flatly
#   toc: true
```

## Adding Content

### New User Guide Page

1. Create a `.qmd` file in `user_guide/`:
   ```markdown
   ---
   title: My New Guide
   ---
   
   Content here...
   ```

2. Rebuild:
   ```bash
   great-docs build
   ```

### Update API Docs

Add or improve docstrings in your code:

```python
def my_function():
    """Brief description.
    
    Detailed explanation here.
    
    Parameters
    ----------
    param : type
        Description
    
    Returns
    -------
    type
        Description
    """
```

Then rebuild.

## File Structure

```
codetyper/
├── great-docs.yml          # Great Docs configuration
├── user_guide/             # User guide pages
│   ├── installation.qmd
│   ├── quickstart.qmd
│   └── script-format.qmd
├── great-docs/             # Build directory (gitignored)
│   └── _site/              # Generated static site
└── .github/
    └── workflows/
        └── docs.yml        # GitHub Actions workflow
```

## Commands Reference

```bash
# Initialize (already done)
great-docs init

# Build documentation
great-docs build
great-docs build --no-refresh  # Skip API re-scan (faster)

# Preview locally
great-docs preview
great-docs preview --port 8000  # Custom port

# Scan API (preview what's documented)
great-docs scan
great-docs scan --verbose

# Setup GitHub Pages (already done)
great-docs setup-github-pages
```

## Tips

1. **Docstring style**: Great Docs uses NumPy style docstrings
2. **Keep it updated**: Run `great-docs build` after code changes
3. **Preview before pushing**: Use `great-docs preview` to check locally
4. **Link between pages**: Use relative links in `.qmd` files
5. **Images**: Add to `user_guide/` and reference with relative paths

## Troubleshooting

### Site not updating on GitHub

1. Check Actions tab for build errors
2. Ensure Pages is set to "GitHub Actions" source
3. Force rebuild: `git commit --allow-empty -m "Rebuild docs" && git push`

### Missing content

1. Check `great-docs build` output for warnings
2. Verify files are in correct locations
3. Run `great-docs scan` to see what's discovered

### Broken links

Fix links in your `.qmd` files to point to actual pages:
```markdown
[Link text](path/to/page.qmd)
```

## Next Steps

1. **Push to GitHub** to enable automatic deployments
2. **Add more guides** as needed (e.g., IDE mode setup, examples)
3. **Set site_url** in `great-docs.yml` once deployed
4. **Share the docs URL** with users!

## Resources

- [Great Docs Documentation](https://posit-dev.github.io/great-docs/)
- [Quarto Documentation](https://quarto.org)
- [GitHub Pages Setup](https://docs.github.com/en/pages)

Built with ❤️ using Great Docs by Posit!
