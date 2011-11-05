# revision 23092
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-ancientgreek
Version:	20111103
Release:	1
Summary:	Ancient Greek hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-ancientgreek.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8
Conflicts:	texlive-texmf <= 20110705-3

%description
Hyphenation patterns for Ancient Greek in LGR and UTF-8
encodings, including support for (obsolete) Ibycus font
encoding. Patterns in UTF-8 use two code positions for each of
the vowels with acute accent (a.k.a tonos, oxia), e.g., U+03AE,
U+1F75 for eta.

%pre
    %_texmf_language_dat_pre
    %_texmf_language_def_pre
    %_texmf_language_lua_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post
    %_texmf_language_lua_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_pre
	%_texmf_language_def_pre
	%_texmf_language_lua_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
	%_texmf_language_lua_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdir}/tex/generic/hyphen/grahyph5.tex
%{_texmfdir}/tex/generic/hyphen/ibyhyph.tex
%_texmf_language_dat_d/hyphen-ancientgreek
%_texmf_language_def_d/hyphen-ancientgreek
%_texmf_language_lua_d/hyphen-ancientgreek
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-ancientgreek <<EOF
%% from hyphen-ancientgreek:
ancientgreek loadhyph-grc.tex
ibycus ibyhyph.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-ancientgreek <<EOF
%% from hyphen-ancientgreek:
\addlanguage{ancientgreek}{loadhyph-grc.tex}{}{1}{1}
\addlanguage{ibycus}{ibyhyph.tex}{}{2}{2}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-ancientgreek <<EOF
-- from hyphen-ancientgreek:
	['ancientgreek'] = {
		loader = 'loadhyph-grc.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-grc.pat.txt',
		hyphenation = '',
	},
	['ibycus'] = {
		loader = 'ibyhyph.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		special = 'disabled:8-bit only',
	},
EOF
