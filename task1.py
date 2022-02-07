"""
* Author: Gaurav Gupta <gauravgupta0045@gmail.com>
* LFX '22 Additional Task-1
"""

# Given that add and mul instructions are seperated by N instruction,
# lets consider N to be 5
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
ops_str = ""

# assignment list for coverpoint
assign_str = ""

# condition list for coverpoint
cond_str = ""

# "?" refers to don't care operations in a coverpoint
dont_care = "?"

# tuple containing instruction that generated coverpoint will target
target_instr = ("add","mul")

dontcare_ops = ' : '.join([item for item in dont_care for i in range(N)])
ops_str = "[" + str(target_instr)+ " : " + dontcare_ops + " : " + str(target_instr) + "]"

def print_coverpoint(label_name, cross_comb_str):
	print(label_name + ":")
	print("  " + str(node_name) + ":")
	print("    - " + str(cross_comb_str).replace("'",""))
	print("\n")

def add_mul_craw():
	label_name = "add_mul_craw"	

	# add some logic for creating assign_str
	assign_lst = []
	assign_str = "[" + str(assign_lst) + "]"

	# add some logic for creating cond_str 
	cond_lst = []
	cond_str = "[" + str(cond_lst) + "]"

	cross_comb_str = ops_str + " :: " + assign_str + " :: " + cond_str
	print_coverpoint(label_name, cross_comb_str)

def add_mul_cnraw():
	label_name = "add_mul_cnraw"	


def add_mul_cwar():
	label_name = "add_mul_cwar"	


def add_mul_cnwar():
	label_name = "add_mul_cnwar"	


def add_mul_cwaw():
	label_name = "add_mul_cwaw"	


def add_mul_cnwaw():
	label_name = "add_mul_cnwaw"	


if __name__ == "__main__":

	# print(ops_str)

	add_mul_craw()
	add_mul_cnraw()
	add_mul_cwar()
	add_mul_cnwar()
	add_mul_cwaw()
	add_mul_cnwaw()

