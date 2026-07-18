%global tl_name mkpic
%global tl_revision 76483
%global tl_bin_links mkpic:%{_texmfdistdir}/scripts/mkpic/mkpic

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.03
Release:	%{tl_revision}.1
Summary:	Perl interface to mfpic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/mkpic
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mkpic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mkpic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(mkpic.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
mkpic provides an easy interface for making small pictures with mfpic.
To this end you create an input file consisting of commands, one per
line, with space separated parameters (or you modify the DATA section of
the mkpic script, which is used if you run it without an input file).
For an extensive description see the file mkpicdoc.pdf, which is part of
the distribution.

