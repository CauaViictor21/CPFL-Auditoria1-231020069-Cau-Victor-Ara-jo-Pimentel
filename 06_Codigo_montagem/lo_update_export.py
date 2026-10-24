# -*- coding: utf-8 -*-
"""Abre um DOCX no LibreOffice (headless), atualiza sumário/índices, salva o DOCX e exporta PDF.
Uso: python lo_update_export.py arquivo.docx"""
import sys, os, subprocess, time, uno
from com.sun.star.beans import PropertyValue

def prop(n, v):
    p = PropertyValue(); p.Name = n; p.Value = v; return p

src = os.path.abspath(sys.argv[1])
port = 2002
proc = subprocess.Popen(["soffice", "--headless", "--invisible", "--norestore",
                         f"--accept=socket,host=localhost,port={port};urp;"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
ctx = None
for _ in range(60):
    try:
        local = uno.getComponentContext()
        resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
        ctx = resolver.resolve(f"uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext")
        break
    except Exception:
        time.sleep(0.5)
smgr = ctx.ServiceManager
desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl(src), "_blank", 0, (prop("Hidden", True),))
idx = doc.getDocumentIndexes(); N_IDX = idx.getCount()
for i in range(idx.getCount()):
    idx.getByIndex(i).update()
doc.refresh()
doc.storeToURL(uno.systemPathToFileUrl(src), (prop("FilterName", "MS Word 2007 XML"),))
pdf = os.path.splitext(src)[0] + ".pdf"
doc.storeToURL(uno.systemPathToFileUrl(pdf), (prop("FilterName", "writer_pdf_Export"),))
try:
    doc.close(True)
except Exception:
    pass
try:
    desktop.terminate()
except Exception:
    pass
try:
    proc.wait(timeout=30)
except Exception:
    proc.kill()
print("indices atualizados:", N_IDX, "| PDF:", pdf)
