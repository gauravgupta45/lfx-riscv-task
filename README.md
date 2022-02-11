# Coverpoint generator to check data hazard
The python script task1.py, will generate all the relevant coverpoints, which can be used to check data hazards in the underlying instruction's execution.

---

### Limitations:
* The source code, for now, is capabale of generating coverpoints for ADD and MUL instructions only.
* It is assumed that the queue, that will contain the op codes, have unique first and last operation. For example if the first operation is add, then last should not be add.
* It is not very much modular yet.

---

### Manual Solution for one coverpoint

Let's condsider the `add_mul_cwaw` coverpoint with the following assembly sequence: (i1 and i6 being the first and last instruction)

```
li x3, 15;
li x4, 4;
add x3,x3,x4;
sllw x5,x6,x3;
srlw x6,x4,x3;
mul x3,x5,x6;
```

There could be a case where x3 from i6 gets written in the pipeline before i3 has completed. We can make use of our software to get rid of this, which is one way to deal with data hazard. We can simple call `nop` operation which is nothing but a fancy way to call `addi x0, x0, 0`. A nop will just advance the program counter (pc), with state of machine being unchanged.

So the assembly sequence will look like this:

```
li x3, 15;
li x4, 4;
add x3,x3,x4;
sllw x5,x6,x3;
srlw x6,x4,x3;
nop
nop
mul x3,x5,x6;
```

A downside of using nop is that it will surely increase latency and program overhead.
