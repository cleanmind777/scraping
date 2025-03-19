require = require('esm')(module);
const xxx = require("puppeteer");

(async () => {

    const browser = await xxx.launch();

    const page = await browser.newPage();
    await page.goto('https://www.w3schools.com/js/tryit.asp?filename=tryjs_events');

    const iframeParagraph = await page.evaluate(() => {

        const iframe = document.getElementById("iframeResult");

        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;

        const iframeP = iframeDoc.getElementById("demo");

        return iframeP.innerHTML;
    });

    console.log(iframeParagraph); // prints "This is a paragraph"

    await browser.close();

})();