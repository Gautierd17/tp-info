	.file	"premierprogramme.c"
	.comm	je_ne_suis_pas_defini, 4, 2
	.comm	variable_de_classe_externe, 4, 2
	.def	__main;	.scl	2;	.type	32;	.endef
	.text
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$48, %rsp
	.seh_stackalloc	48
	.seh_endprologue
	call	__main
	movl	$3, -4(%rbp)
	leaq	variable_de_classe_externe(%rip), %rax
	movl	$2, (%rax)
	leaq	je_ne_suis_pas_defini(%rip), %rax
	movl	(%rax), %eax
	addl	%eax, -4(%rbp)
	leaq	variable_de_classe_externe(%rip), %rax
	movl	(%rax), %eax
	movl	-4(%rbp), %edx
	subl	%eax, %edx
	movl	%edx, %eax
	addq	$48, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (tdm64-1) 5.1.0"
