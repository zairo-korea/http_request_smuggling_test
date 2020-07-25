<?php
echo "<h1>It's works!</h1><br>\n";
echo "<pre>";
if (!function_exists('getallheaders')) {

    function getallheaders() {
        $headers = array();
        foreach ($_SERVER as $name => $value) {
            if (substr($name, 0, 5) == 'HTTP_') {
                $headers[str_replace(' ', '-', ucwords(strtolower(str_replace('_', ' ', substr($name, 5)))))] = $value;
            }
        }
        return $headers;
    }

}
echo "<h2>[HTTP Headers]</h2>";
var_dump(getallheaders());
$data = file_get_contents("php://input");
echo "<h2>[HTTP Body]</h2>";
print_r($data);
echo "</pre>";