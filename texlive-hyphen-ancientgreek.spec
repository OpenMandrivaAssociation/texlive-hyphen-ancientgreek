%global tl_name hyphen-ancientgreek
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Ancient Greek hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-ancientgreek
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-ancientgreek.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Ancient Greek in LGR and UTF-8 encodings,
including support for (obsolete) Ibycus font encoding. Patterns in UTF-8
use two code positions for each of the vowels with acute accent (a.k.a
tonos, oxia), e.g., U+03AE, U+1F75 for eta.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-ancientgreek:
ancientgreek loadhyph-grc.tex
ibycus ibyhyph.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-ancientgreek:
\addlanguage{ancientgreek}{loadhyph-grc.tex}{}{1}{1}
\addlanguage{ibycus}{ibyhyph.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-ancientgreek:
['ancientgreek'] = {
	loader = 'loadhyph-grc.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-grc.pat.txt',
},
['ibycus'] = {
	loader = 'ibyhyph.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	special = '"disabled:8-bit',
},
TL_HYPHEN_EOF
