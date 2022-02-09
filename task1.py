"""
* Author: Gaurav Gupta <gauravgupta0045@gmail.com>
* LFX '22 Additional Task-1
"""

# Given that add and mul instructions are seperated by N instruction,
# lets consider N to be 2
N = 2

# Total instructions, which is also window length and queue size
queue_len = N + 2

# label name, for each scenarios
label_name = ""

# node name
node_name = "cross_comb"

# cross_comb_str list, which will be our final result for one label
cross_comb_str = ""

# opcodes str for coverpoint
str_ops = ""

# assignment list for coverpoint
assign_str = ""

# condition list for coverpoint
str_cond = ""

# "?" refers to don't care operations in a coverpoint
dont_care = "?"

# tuple containing instruction that generated coverpoint will target
target_instr = "(add,mul)"

dontcare_ops = ' : '.join([item for item in dont_care for i in range(N)])
str_ops = "[" + target_instr + " : " + dontcare_ops + " : " + target_instr + "]"

def print_coverpoint(label_name, cross_comb_str):
	print(label_name + ":")
	print("  " + str(node_name) + ":")
	print("    - " + str(cross_comb_str).replace("'",""))
	print("\n")

def add_mul_craw():
	label_name = "add_mul_craw"	

	# since, write is happening first followed by read -- RAW -- we will assign the destination reg to a.
	assign_dest_reg = "a=rd : "

	# rest of the assigns will be don't care, as we are reading.
	dontcare_assign = ' : '.join([item for item in dont_care for i in range(queue_len-1)])
	str_assign = "[" + assign_dest_reg + dontcare_assign + "]"

	# since this is a consuming inst, we need to compare src reg with rd of previous instr.
	src_reg_cond = "rs1==a or rs2==a"
	str_src_reg_cond = ""
	for i in range(queue_len-1):
		str_src_reg_cond += " : " + src_reg_cond

	# first instruction's condition check will always be don't care, rest all will be checking the source reg
	dontcare_cond = dont_care

	str_cond = "[" + dontcare_cond + str_src_reg_cond + "]"

	# create the final cross_comb_str
	cross_comb_str = str_ops + " :: " + str_assign + " :: " + str_cond
	print_coverpoint(label_name, cross_comb_str)

def add_mul_ncraw():
	label_name = "add_mul_ncraw"

	# since, write is happening first followed by read -- RAW -- we will assign the destination reg to a.
	assign_dest_reg = "a=rd : "

	# rest of the assigns will be don't care, as we are reading.
	dontcare_assign = ' : '.join([item for item in dont_care for i in range(queue_len-1)])
	assign_str = "[" + assign_dest_reg + dontcare_assign + "]"

	# since this is a non-consuming inst, result of prev instruction doesn't matter.
	cond_src_reg = "rs1==a or rs2==a"
	cond_str_src_reg = ""
	for i in range(1):
		cond_str_src_reg += " : " + cond_src_reg

	# for non-consuming instructions, all checks except last, are don't care
	dontcare_cond = ' : '.join([item for item in dont_care for i in range(queue_len-1)])

	str_cond = "[" + dontcare_cond + cond_str_src_reg + "]"

	# create the final cross_comb_str
	cross_comb_str = str_ops + " :: " + assign_str + " :: " + str_cond
	print_coverpoint(label_name, cross_comb_str)


def add_mul_cwar():
	label_name = "add_mul_cwar"


def add_mul_ncwar():
	label_name = "add_mul_ncwar"


def add_mul_cwaw():
	label_name = "add_mul_cwaw"


def add_mul_ncwaw():
	label_name = "add_mul_ncwaw"


if __name__ == "__main__":

	add_mul_craw()
	add_mul_ncraw()
	add_mul_cwar()
	add_mul_ncwar()
	add_mul_cwaw()
	add_mul_ncwaw()

