var fs = require("fs");
var http = require("http");
var os = require("os");
var ip = require("ip");

var server = http.createServer(function(req, res){
    if (req.url === "/"){
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
        })
    }

    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        
        var totalMemory=os.totalmem();
        var mbTotMem = totalMemory/1000000


        var freeMemory=os.freemem();
        var mbFreeMem = freeMemory/1000000
        cpuCount=os.cpus().length
        //GeeksforGeeks.com for help with conversion.
        var sec = os.uptime(); 
        var min = sec/60; 
        var hour = min/60; 
        var day = hour/24;
        
        sec = Math.floor(sec); 
        min = Math.floor(min); 
        hour = Math.floor(hour); 
        day = Math.floor(day);
        
        day = day%24;
        hour = hour%60; 
        min = min%60; 
        sec = sec%60; 



        
        
        
        html=`
        <!DOCTYPE html>
        <head>
            <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName} </p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: Days: ${day}, Hours: ${hour}, Minutes: ${min}, Seconds: ${sec}</p>
            <p>Total Memory: ${mbTotMem} MB</p>
            <p>Free Memory: ${mbFreeMem} MB</p>
            <p>Number of CPUs: ${cpuCount} </p>
        </body>
        </html>
        `
        res.writeHead(200, {"Content-Type" : "text/html"});
        res.end(html);
    }

    else{
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
});

server.listen(3000);

console.log("Server listening on port 3000");