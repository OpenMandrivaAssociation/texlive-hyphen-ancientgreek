# revision 29725
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-ancientgreek
Version:	20131012
Release:	9
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

%description
Hyphenation patterns for Ancient Greek in LGR and UTF-8
encodings, including support for (obsolete) Ibycus font
encoding. Patterns in UTF-8 use two code positions for each of
the vowels with acute accent (a.k.a tonos, oxia), e.g., U+03AE,
U+1F75 for eta.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyphen/grahyph5.tex
%{_texmfdistdir}/tex/generic/hyphen/ibyhyph.tex
%_texmf_language_dat_d/hyphen-ancientgreek
%_texmf_language_def_d/hyphen-ancientgreek
%_texmf_language_lua_d/hyphen-ancientgreek

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-ancientgreek <<EOF
\%% from hyphen-ancientgreek:
ancientgreek loadhyph-grc.tex
ibycus ibyhyph.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-ancientgreek
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-ancientgreek <<EOF
\%% from hyphen-ancientgreek:
\addlanguage{ancientgreek}{loadhyph-grc.tex}{}{1}{1}
\addlanguage{ibycus}{ibyhyph.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-ancientgreek
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
