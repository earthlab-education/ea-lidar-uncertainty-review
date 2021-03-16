# Pull Request Template

## Review Checklist

## CI Checks
- [ ] The notebook runs from start to finish on all operating systems:
   - [ ] Mac
   - [ ] Windows
   - [ ] Linux 
### Reproducibility
- [ ] Are the data downloaded in the code
- [ ] Are paths created to ensure they work on all operating systems (using  os.path.join)
- [ ] Are comments used to clarify the contents of the code that can’t be clarified using expressive variable and function names alone? (not too many comments - just enough)
- [ ] Does the notebook run from start to finish?

### PEP 8 standards & Code Readability
### Functions
- [ ] Do functions follow PEP 8 format conventions?
- [ ] Are function docstrings clear (all  inputs and outputs clearly  described and defined)
- [ ] Are function names expressive (the name describes what the function does)?
- [ ] Are functions easy to understand and read?
- [ ] How many tasks does each function do? (ideally a function does one thing well).
### Package imports
- [ ] Are standard modules (those included with the base  python install) vs. third party (related but externally developed tools) import groups correct with appropriate spacing in between each group?
- [ ] Are variable names throughout the code, expressive?
- [ ] Suggest changes if not, highlight what was done well
- [ ] Is the code overall easy to understand and read? Are there things that would make it more clear / cleaner?

### DRY Code
- [ ] Are segments of code repeated in the file or is the code DRY?
- [ ] Are loops used to optimize DRY code?
- [ ] Are functions used to optimize DRY code?
- [ ] Are there any areas that could be potentially improved (you can suggest improvements OR you can just highlight parts of the code where you suspect it could  be cleaner / more efficient.

### Novel Approaches to Problem solving
- [ ] Highlight any novel approaches to completing the assignment.
