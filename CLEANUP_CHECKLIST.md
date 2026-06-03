# Pre-Push Cleanup Checklist

Files to review before pushing to GitHub.

## ✅ Files to DELETE (Old/Redundant)

### Legacy single-file versions
These have been replaced by the modular package in `src/codetyper/`:

- [ ] `codetyper.py` - Old single-file version (~34KB)
- [ ] `config_schema.py` - Old config module (~1KB)

**Why delete:** The new modular package in `src/codetyper/` replaces these entirely. Keeping them will cause confusion.

**To delete:**
```bash
rm codetyper.py config_schema.py
```

## 📝 Files to KEEP

### Documentation (all useful)
- ✅ `README.md` - Main documentation (updated)
- ✅ `QUICKSTART.md` - Quick start guide (updated)
- ✅ `INSTALL.md` - Installation guide
- ✅ `DISTRIBUTION.md` - Distribution guide
- ✅ `PACKAGING_SUMMARY.md` - Package structure overview
- ✅ `DOCS_SETUP.md` - Documentation website setup
- ✅ `WEBSITE_SUMMARY.md` - Website overview
- ✅ `CLEANUP_CHECKLIST.md` - This file

### Configuration
- ✅ `pyproject.toml` - Package configuration
- ✅ `requirements.txt` - Dependencies
- ✅ `great-docs.yml` - Docs configuration
- ✅ `LICENSE` - MIT License
- ✅ `.gitignore` - Git ignore patterns

### Code
- ✅ `src/codetyper/` - New modular package (11 files)
- ✅ `examples/` - Example scripts
- ✅ `tests/` - Test directory
- ✅ `user_guide/` - User guide pages
- ✅ `.github/workflows/` - CI/CD workflows

## 🤔 Optional: Consolidate Documentation

You have **7 documentation files** in the root. Consider consolidating:

### Option 1: Keep All (Recommended for now)
Each serves a specific purpose and users can navigate to what they need.

### Option 2: Consolidate Later
After GitHub Pages is live, you could:
- Keep `README.md` (links to website)
- Keep `QUICKSTART.md` (for quick reference)
- Archive others in a `docs/` folder

## 📊 File Size Summary

```
Old files to delete:
├── codetyper.py          ~34 KB
└── config_schema.py      ~1 KB
                          ------
Total saved:              ~35 KB

Documentation to keep:    ~40 KB
New package code:         ~15 KB
```

## ⚡ Quick Cleanup Commands

```bash
# Delete old legacy files
rm codetyper.py config_schema.py

# Verify modular package works
codetyper --help

# Check git status
git status
```

## ✨ After Cleanup

Your repository will have:
- ✅ Clean structure (no duplicate files)
- ✅ Only the modular package
- ✅ Clear documentation
- ✅ Ready for GitHub Pages

## 🎯 Recommended Action

**Delete the 2 legacy files** before pushing:

```bash
rm codetyper.py config_schema.py
git status  # Verify they're gone
```

This keeps your repo clean and avoids confusion about which version to use!
