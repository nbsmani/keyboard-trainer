"""Build ../index.html (single self-contained page) from src/trainer.html.

Requires: npm i abcjs@6.7.2 esbuild  (run in src/)
Inlines abcjs + instrument samples and lowers JS to ES2017 for older iPad Safari.
"""
import re, subprocess, pathlib
here = pathlib.Path(__file__).parent
s = (here / "trainer.html").read_text()
def lower(js):
    r = subprocess.run(["npx", "esbuild", "--loader=js", "--target=es2017"], input=js, capture_output=True, text=True, cwd=here)
    if r.returncode: raise SystemExit(r.stderr)
    return r.stdout
s = re.sub(r"<script>(.*?)</script>", lambda m: "<script>" + lower(m.group(1)) + "</script>", s, flags=re.S)
abc = subprocess.run(["npx", "esbuild", "node_modules/abcjs/dist/abcjs-basic-min.js", "--target=es2017", "--minify"],
                     capture_output=True, text=True, cwd=here, check=True).stdout.replace("</script", "<\\/script")
snd = "".join("<script>" + (here / "sounds" / f"{n}.js").read_text() + "</script>\n"
              for n in ["piano", "flute", "violin", "clarinet", "organ", "guitar-acoustic"])
tag = '<script src="https://cdn.jsdelivr.net/npm/abcjs@6.7.2/dist/abcjs-basic-min.js"></script>'
assert tag in s
s = s.replace(tag, "<script>" + abc + "</script>\n" + snd)
(here.parent / "index.html").write_text(s)
print("wrote index.html", len(s) // 1024, "KB")
