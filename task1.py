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
cond_str = ""

# "?" refers to don't care operations in a coverpoint
dontcare = "?"

# tuple containing instruction that generated coverpoint will target
target_instr = "(add,mul)"

dontcare_ops = ' : '.join([item for item in dontcare for i in range(N)])
str_ops = "[" + target_instr + " : " + dontcare_ops + " : " + target_instr + "]"


def print_coverpoint(label_name, cross_comb_str):
	print(label_name + ":")
	print("  " + str(node_name) + ":")
	print("    - " + str(cross_comb_str).replace("'",""))
	print("\n")


def add_mul_crar():
	label_name = "add_mul_crar"

	# since, read is happening first, we will assign the source reg(s) to a/b. And dest reg will be stored in c
	assign_src_reg = "a=rs1; b=rs2; c=rd : "

	# rest of the assigns will be don't care.
	assign_dontcare = ' : '.join([item for item in dontcare for i in range(queue_len-1)])
	assign_str = "[" + assign_src_reg + assign_dontcare + "]"


	# first instruction's condition check will always be don't care, rest all will be checking the source reg
	cond_dontcare = dontcare

	# since this is a consuming inst, we need to compare src reg with rd of first instr.
	cond_src_reg = "rs1==c or rs2==c"
	cond_src_reg_str = ""
	for i in range(queue_len-2):
		cond_src_reg_str += " : " + cond_src_reg

	# since its a RAR, we need to check the source reg of last
	# instruction if they are equal to any of source reg of first instr.
	cond_dest_reg = " : (rs1==a or rs2==a or rs1==b or rs2==b)"

	cond_str = "[" + cond_dontcare + cond_src_reg_str + cond_dest_reg + "]"

	# create the final cross_comb_str
	cross_comb_str = str_ops + " :: " + assign_str + " :: " + cond_str
	print_coverpoint(label_name, cross_comb_str)


def add_mul_ncrar():
	label_name = "add_mul_ncrar"

	# since, read is happening first followed by read -- RAR -- we will assign the source reg(s) to a/b.
	assign_src_reg = "a=rs1; b=rs2 : "

	# rest of the assigns will be don't care.
	assign_dontcare = ' : '.join([item for item in dontcare for i in range(queue_len-1)])
	assign_str = "[" + assign_src_reg + assign_dontcare + "]"


	# since this is a non-consuming instr, result of prev instruction doesn't matter.
	cond_dontcare = ' : '.join([item for item in dontcare for i in range(queue_len-1)])

	# since its a RAR, we need to check the source reg of last
	# instruction if they are equal to any of source reg of first instr.
	cond_dest_reg = " : (rs1==a or rs2==a or rs1==b or rs2==b)"

	cond_str = "[" + cond_dontcare + cond_dest_reg + "]"

	# create the final cross_comb_str
	cross_comb_str = str_ops + " :: " + assign_str + " :: " + cond_str
	print_coverpoint(label_name, cross_comb_str)


def add_mul_craw():
	label_name = "add_mul_craw"	

	# since, write is happening first, we will assign the destination reg to a.
	assign_dest_reg = "a=rd : "

	# rest of the assigns will be don't care.
	assign_dontcare = ' : '.join([item for item in dontcare for i in range(queue_len-1)])
	assign_str = "[" + assign_dest_reg + assign_dontcare + "]"


	# first instruction's condition check will always be don't care, rest all will be checking the source reg
	cond_dontcare = dontcare

	# since this is a consuming instr, we need to compare src reg with rd of first instr.
	cond_src_reg = "rs1==a or rs2==a"
	cond_src_reg_str = ""
	for i in range(queue_len-2):
		cond_src_reg_str += " : " + cond_src_reg

	# since its a RAW, we need to check the source register(s) of last
	# instruction if they are equal to dest reg of first instr.
	cond_dest_reg = "rs1==a or rs2==a"
	cond_dest_reg_str = ""
	for i in range(1):
		cond_dest_reg_str += " : " + cond_dest_reg

	cond_str = "[" + cond_dontcare + cond_src_reg_str + cond_dest_reg_str + "]"

	# create the final cross_comb_str
	cross_comb_str = str_ops + " :: " + assign_str + " :: " + cond_str
	print_coverpoint(label_name, cross_comb_str)

def add_mul_ncraw():
	label_name = "add_mul_ncraw"

	# since, write is happening first, we will assign the destination reg to a.
	assign_dest_reg = "a=rd : "

	# rest of the assigns will be don't care
	assign_dontcare = ' : '.join([item for item in dontcare for i in range(queue_len-1)])
	assign_str = "[" + assign_dest_reg + assign_dontcare + "]"


	# since its a RAW, we need to check the source register(s) of last
	# instruction if they are equal to dest reg of first instr.
	cond_src_reg = "rs1==a or rs2==a"
	cond_src_reg_str = ""
	for i in range(1):
		cond_src_reg_str += " : " + cond_src_reg

	# since this is a non-consuming instr, result of prev instruction doesn't matter.
	cond_dontcare = ' : '.join([item for item in dontcare for i in range(queue_len-1)])

	cond_str = "[" + cond_dontcare + cond_src_reg_str + "]"

	# create the final cross_comb_str
	cross_comb_str = str_ops + " :: " + assign_str + " :: " + cond_str
	print_coverpoint(label_name, cross_comb_str)


def add_mul_cwar():
	label_name = "add_mul_cwar"

	# since, read is happening first, will assign the source reg(s) to a/b.
	assign_src_reg = "a=rs1; b=rs2; c=rd : "

	# rest of the assigns will be don't care.
	assign_dontcare = ' : '.join([item for item in dontcare for i in range(queue_len-1)])
	assign_str = "[" + assign_src_reg + assign_dontcare + "]"


	# first instruction's condition check will always be don't care, rest all will be checking the source reg
	cond_dontcare = dontcare

	# since this is a consuming instr, we need to compare src reg with rd of first instr.
	cond_src_reg = "rs1==c or rs2==c"
	cond_src_reg_str = ""
	for i in range(queue_len-2):
		cond_src_reg_str += " : " + cond_src_reg

	# since its a WAR, we need to check the destination register of last
	# instruction if they are equal to any of source reg of first instr.
	cond_dest_reg = " : rd==a or rd==b"

	cond_str = "[" + cond_dontcare + cond_src_reg_str + cond_dest_reg + "]"

	# create the final cross_comb_str
	cross_comb_str = str_ops + " :: " + assign_str + " :: " + cond_str
	print_coverpoint(label_name, cross_comb_str)


def add_mul_ncwar():
	label_name = "add_mul_ncwar"

	# since, read is happening first, we will assign the source reg(s) to a/b.
	assign_src_reg = "a=rs1; b=rs2 : "

	# rest of the assigns will be don't care.
	assign_dontcare = ' : '.join([item for item in dontcare for i in range(queue_len-1)])
	assign_str = "[" + assign_src_reg + assign_dontcare + "]"


	# since this is a non-consuming instr, result of prev instruction doesn't matter.
	cond_dontcare = ' : '.join([item for item in dontcare for i in range(queue_len-1)])

	# since its a WAR, we need to check the destination reg of last
	# instruction if they are equal to any of source reg of first instr.
	cond_dest_reg = " : rd==a or rd==b"

	cond_str = "[" + cond_dontcare + cond_dest_reg + "]"

	# create the final cross_comb_str
	cross_comb_str = str_ops + " :: " + assign_str + " :: " + cond_str
	print_coverpoint(label_name, cross_comb_str)


def add_mul_cwaw():
	label_name = "add_mul_cwaw"

	# since, write is happening first, we will assign the destination reg to a.
	assign_dest_reg = "a=rd : "

	# rest of the assigns will be don't care.
	assign_dontcare = ' : '.join([item for item in dontcare for i in range(queue_len-1)])
	assign_str = "[" + assign_dest_reg + assign_dontcare + "]"


	# first instruction's condition check will always be don't care, rest all will be checking the source reg
	cond_dontcare = dontcare

	# since this is a consuming inst, we need to compare src reg with rd of first instr.
	cond_src_reg = "rs1==a or rs2==a"
	cond_src_reg_str = ""
	for i in range(queue_len-2):
		cond_src_reg_str += " : " + cond_src_reg

	# since its a WAW, we need to check the destination reg of last
	# instruction if it is equal to the destination reg of first instr.
	cond_dest_reg = " : rd==a"

	cond_str = "[" + cond_dontcare + cond_src_reg_str + cond_dest_reg + "]"

	# create the final cross_comb_str
	cross_comb_str = str_ops + " :: " + assign_str + " :: " + cond_str
	print_coverpoint(label_name, cross_comb_str)


def add_mul_ncwaw():
	label_name = "add_mul_ncwaw"

	# since, write is happening first, we will assign the destination reg to a.
	assign_dest_reg = "a=rd : "

	# rest of the assigns will be don't care.
	assign_dontcare = ' : '.join([item for item in dontcare for i in range(queue_len-1)])
	assign_str = "[" + assign_dest_reg + assign_dontcare + "]"


	# since this is a non-consuming instr, result of prev instruction doesn't matter.
	cond_dontcare = ' : '.join([item for item in dontcare for i in range(queue_len-1)])

	# since its a WAW, we need to check the destination reg of last
	# instruction if it is equal to the destination reg of first instr.
	cond_dest_reg = " : rd==a"

	cond_str = "[" + cond_dontcare + cond_dest_reg + "]"

	# create the final cross_comb_str
	cross_comb_str = str_ops + " :: " + assign_str + " :: " + cond_str
	print_coverpoint(label_name, cross_comb_str)



if __name__ == "__main__":

	add_mul_crar()
	add_mul_ncrar()
	add_mul_craw()
	add_mul_ncraw()
	add_mul_cwar()
	add_mul_ncwar()
	add_mul_cwaw()
	add_mul_ncwaw()

