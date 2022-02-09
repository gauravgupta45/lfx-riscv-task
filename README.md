# Generate data hazard coverpoint
The python script task1.py, will generate all the relevant coverpoints, which can be used to check data hazards in the underlying instruction's execution.

---

### Limitations:
* The source code, for now, is capabale of generating coverpoints for ADD and MUL instructions only.
* It is assumed that the queue, that will contain the op codes, have unique first and last operation. For example if the first operation is add, then last should not be add.

---

### Manual Solution for one coverpoint

