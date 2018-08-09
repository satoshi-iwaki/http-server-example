# encoding: UTF-8
#!usr/bin/env ruby

require 'webrick/https'

class HelloServlet < HTTPServlet::AbstractServlet
    @@mutex = Mutex.new

    def do_POST(req, res)
        logger = WEBrick::BasicLog.new()
        logger << "------------ Request  --------------"
        logger << req
        logger << "------------------------------------"

        digest = OpenSSL::Digest::SHA256.hexdigest(req.body)
        res.status = 200
        res.body = "{\"content\" : \"#{req.body}\", \"digest\" : \"#{digest}\"}"
        res['Content-Type'] = "application/json"
        logger << "------------ Response --------------"
        logger << res
        logger << "------------------------------------"
    end
end
$server.mount("/api/digest", HelloServlet)
