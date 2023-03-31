Name:		texlive-mkpic
Version:	33700
Release:	2
Summary:	Perl interface to mfpic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/mkpic
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkpic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkpic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-mkpic.bin = %{EVRD}

%description
A Perl interface to mfpic making it possible to enter simple
commands with tab separated arguments and without
braces/brackets to design figures. The script produces a style
file, mkpic.sty, containing one LaTeX command for each picture.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/mkpic
%{_texmfdistdir}/scripts/mkpic/mkpic
%doc %{_texmfdistdir}/doc/support/mkpic/README
%doc %{_texmfdistdir}/doc/support/mkpic/mkpic.pdf
%doc %{_texmfdistdir}/doc/support/mkpic/mkpicdoc.pdf
%doc %{_texmfdistdir}/doc/support/mkpic/mkpicdoc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/mkpic/mkpic mkpic
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
