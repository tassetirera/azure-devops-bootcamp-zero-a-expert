import os
import glob
base = r"c:\Users\mouss\source\repos\azure-devops-bootcamp-zero-a-expert\Documentations\CERTIFICATION-AZURE\Themes"
missing = []
for theme in sorted(os.listdir(base)):
    tdir = os.path.join(base, theme)
    if not os.path.isdir(tdir):
        continue
    for path in sorted(glob.glob(os.path.join(tdir, 'QCM-*.md'))):
        txt = open(path, 'r', encoding='utf-8').read()
        has_corr = '## Corrections détaillées' in txt
        if not has_corr:
            missing.append((path, 'missing section'))
            continue
        after = txt.split('## Corrections détaillées', 1)[1]
        has_expl = any(line.strip().startswith('-') for line in after.splitlines() if line.strip())
        if not has_expl:
            missing.append((path, 'missing explanations'))

for path, reason in missing:
    print(f"{path}	{reason}")
print(f"Total missing: {len(missing)}")
