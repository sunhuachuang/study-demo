	.text
	.file	"test.cgu-0.rs"
	.section	.text._ZN4test4main17h916a53db53ad90a1E,"ax",@progbits
	.p2align	4, 0x90
	.type	_ZN4test4main17h916a53db53ad90a1E,@function
_ZN4test4main17h916a53db53ad90a1E:
	.cfi_startproc
	pushq	%rax
.Lcfi0:
	.cfi_def_cfa_offset 16
	movl	$1, %edi
	movl	$2, %esi
	callq	_ZN4test3sum17hda100ba9dfb6af59E
	movl	%eax, 4(%rsp)
	popq	%rax
	retq
.Lfunc_end0:
	.size	_ZN4test4main17h916a53db53ad90a1E, .Lfunc_end0-_ZN4test4main17h916a53db53ad90a1E
	.cfi_endproc

	.section	.text._ZN4test3sum17hda100ba9dfb6af59E,"ax",@progbits
	.p2align	4, 0x90
	.type	_ZN4test3sum17hda100ba9dfb6af59E,@function
_ZN4test3sum17hda100ba9dfb6af59E:
	.cfi_startproc
	pushq	%rax
.Lcfi1:
	.cfi_def_cfa_offset 16
	addl	%esi, %edi
	seto	%al
	testb	$1, %al
	movl	%edi, 4(%rsp)
	jne	.LBB1_2
	movl	4(%rsp), %eax
	popq	%rcx
	retq
.LBB1_2:
	leaq	panic_loc.2(%rip), %rax
	movq	%rax, %rdi
	callq	_ZN4core9panicking5panic17hfdadbcda5c7d3c71E@PLT
.Lfunc_end1:
	.size	_ZN4test3sum17hda100ba9dfb6af59E, .Lfunc_end1-_ZN4test3sum17hda100ba9dfb6af59E
	.cfi_endproc

	.section	.text.main,"ax",@progbits
	.globl	main
	.p2align	4, 0x90
	.type	main,@function
main:
	.cfi_startproc
	subq	$24, %rsp
.Lcfi2:
	.cfi_def_cfa_offset 32
	leaq	_ZN4test4main17h916a53db53ad90a1E(%rip), %rax
	movq	%rdi, 16(%rsp)
	movq	%rax, %rdi
	movq	16(%rsp), %rax
	movq	%rsi, 8(%rsp)
	movq	%rax, %rsi
	movq	8(%rsp), %rdx
	callq	_ZN3std2rt10lang_start17h850ce0a66536d380E@PLT
	addq	$24, %rsp
	retq
.Lfunc_end2:
	.size	main, .Lfunc_end2-main
	.cfi_endproc

	.type	str.0,@object
	.section	.rodata.str.0,"a",@progbits
str.0:
	.ascii	"test.rs"
	.size	str.0, 7

	.type	str.1,@object
	.section	.rodata.str.1,"a",@progbits
	.p2align	4
str.1:
	.ascii	"attempt to add with overflow"
	.size	str.1, 28

	.type	panic_loc.2,@object
	.section	.data.rel.ro.panic_loc.2,"aw",@progbits
	.p2align	3
panic_loc.2:
	.quad	str.1
	.quad	28
	.quad	str.0
	.quad	7
	.long	6
	.zero	4
	.size	panic_loc.2, 40


	.section	".note.GNU-stack","",@progbits
