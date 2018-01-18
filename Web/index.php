<!DOCTYPE HTML>
<html>
    <head>
        <title>Perseus Mobile</title>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
    
        <div class="header">
            Perseus Mobile
        </div>
        <nav>
            <a>Texts</a>
            <a>Dictionary</a>
        </nav>
        <div class="search">
            <input type="text" />
        </div>
        <div class="text1">
            <?php echo("dfwkwjeipee"); ?>
        </div>
        <div class="text2">

        </div>
    
        <?php

$doc = new DOMDocument;
$doc->load("http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133");
$xpath = new DOMXpath($doc);
$elements = $xpath->query("*/div[@id='text']");

#echo("kekek$elements");
?>
    </body>
    
</html>