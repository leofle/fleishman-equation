// Renders $$...$$ and $...$ with KaTeX into paper.html, then prints to PDF with Playwright/Chromium.
const fs=require('fs'),path=require('path'),katex=require('katex');
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
let s=fs.readFileSync('paper.src.html','utf8');
const [head,body]=s.split('<body>');
let b=body.replace(/\$\$([\s\S]+?)\$\$/g,(_,m)=>katex.renderToString(m,{displayMode:true,throwOnError:true}))
          .replace(/\$([^$\n]+?)\$/g,(_,m)=>katex.renderToString(m,{throwOnError:true}));
fs.writeFileSync('paper.html',head+'<body>'+b);
(async()=>{const br=await chromium.launch();const p=await br.newPage();
await p.goto('file://'+path.resolve('paper.html'));await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:'rogue_misuse_decomposition_whitepaper.pdf',format:'Letter',preferCSSPageSize:true,displayHeaderFooter:true,
headerTemplate:'<div style="font-size:7.5pt;font-family:Source Serif Pro,serif;color:#666;width:100%;text-align:center;padding-top:0.45in">L. Fleishman &middot; The Rogue&ndash;Misuse Decomposition &middot; White paper, not peer reviewed</div>',
footerTemplate:'<div style="font-size:8pt;font-family:Source Serif Pro,serif;color:#444;width:100%;text-align:center;padding-bottom:0.35in"><span class="pageNumber"></span> / <span class="totalPages"></span></div>'});
await br.close();
// Chromium sets Title from <title> but no Author; add it with pdf-lib if available.
try{const {PDFDocument}=require('pdf-lib');const out='rogue_misuse_decomposition_whitepaper.pdf';const d=await PDFDocument.load(fs.readFileSync(out));d.setAuthor('L. Fleishman');fs.writeFileSync(out,await d.save());}catch(e){console.warn('Author metadata not set:',e.message);}
})();
