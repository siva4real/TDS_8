---
marp: true
theme: custom
paginate: true
math: mathjax
header: 'Product Documentation - Tech Writer Demo'
footer: 'Contact: 24f3004072@ds.study.iitm.ac.in'
---

<!-- Define custom theme -->
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

:root {
  --color-background: #f8f9fa;
  --color-foreground: #2d3748;
  --color-accent: #3182ce;
  --color-secondary: #e2e8f0;
}

section {
  background-color: var(--color-background);
  color: var(--color-foreground);
  font-family: 'Inter', sans-serif;
  padding: 40px;
}

h1, h2, h3 {
  color: var(--color-accent);
  margin-bottom: 20px;
}

.highlight-box {
  background-color: var(--color-secondary);
  padding: 20px;
  border-radius: 8px;
  border-left: 4px solid var(--color-accent);
  margin: 20px 0;
}

.math-equation {
  background-color: rgba(255, 255, 255, 0.9);
  padding: 15px;
  border-radius: 6px;
  margin: 10px 0;
  font-size: 1.2em;
}
</style>

# Product Documentation Presentation

## Overview

Welcome to our comprehensive product documentation presentation.

**Contact Information:**
- Email: 24f3004072@ds.study.iitm.ac.in

<div class="highlight-box">
This presentation demonstrates maintainable documentation practices using Marp Markdown.
</div>

---

<!-- _backgroundColor: #667eea -->
<!-- _color: white -->

# Custom Theming & Styling

## Marp Directives in Action

This slide showcases custom styling with Marp directives:

- **Background color** set via `<!-- _backgroundColor: #667eea -->`
- **Text color** set via `<!-- _color: white -->`
- **Custom CSS classes** for enhanced presentation

<div class="highlight-box" style="background-color: rgba(255, 255, 255, 0.1); color: white; border-left-color: #ffd700;">
Key features of maintainable documentation:
- Version control friendly
- Easy format conversion
- Consistent styling
</div>

---

![bg](https://images.unsplash.com/photo-1555949963-aa79dcee981c?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80)

# Background Images

## Visual Documentation

This slide features a beautiful background image from Unsplash, demonstrating how Marp can incorporate visual elements.

**Benefits of visual documentation:**
- Improved user engagement
- Better information retention
- Professional presentation quality

<div class="highlight-box" style="background-color: rgba(0, 0, 0, 0.7); color: white; border-left-color: #ffd700;">
The background image directive: `![bg](image-url)` allows seamless integration of visuals.
</div>

---

# Mathematical Equations

## Algorithmic Complexity Analysis

Mathematical notation is crucial for technical documentation:

<div class="math-equation">
**Time Complexity of Binary Search:**

$$O(\log n)$$

**Formula:**
$$T(n) = T\left(\frac{n}{2}\right) + O(1)$$
</div>

<div class="math-equation">
**Big O Notation Examples:**

| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Linear Search | $O(1)$ | $O(n)$ | $O(n)$ |
| Binary Search | $O(1)$ | $O(\log n)$ | $O(\log n)$ |
| Bubble Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ |

</div>

---

<!-- _backgroundColor: #2d3748 -->
<!-- _color: white -->

# Advanced Features

## Marp Capabilities

<div class="highlight-box" style="background-color: rgba(255, 255, 255, 0.1); color: white; border-left-color: #ffd700;">

**Marp Features Demonstrated:**
- ✅ Custom themes with CSS variables
- ✅ Page numbering (check footer)
- ✅ Background images
- ✅ Mathematical equations with MathJax
- ✅ Custom styling directives
- ✅ Professional typography

</div>

**Conversion Options:**
- PDF export: `marp presentation.md --pdf`
- HTML export: `marp presentation.md --html`
- PPTX export: `marp presentation.md --pptx`

---

# Thank You

## Questions & Contact

For more information about our documentation practices:

📧 **Email:** 24f3004072@ds.study.iitm.ac.in

<div class="highlight-box">
This presentation was created using Marp Markdown for maintainable, version-controlled documentation that can be easily converted to multiple formats.
</div>
