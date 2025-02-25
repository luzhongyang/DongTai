######################################################################
# @author      : bidaya0 (bidaya0@$HOSTNAME)
# @file        : test_agent_method_pool
# @created     : 星期一 12月 13, 2021 17:21:33 CST
#
# @description :
######################################################################


from test.apiserver.test_agent_base import AgentTestCase,gzipdata
from dongtai_common.models.agent import IastAgent
from dongtai_common.models.agent_method_pool import MethodPool
import gzip
import base64

class AgentMethodPoolTestCase(AgentTestCase):

    def test_agent_method_pool_upload(self):
        method = {
            "detail": {
                "agentId":
                3490,
                "clientIp":
                "172.19.0.3",
                "language":
                "PHP",
                "method":
                "POST",
                "pool": [{
                    "args": "",
                    "callerClass": "",
                    "callerLineNumber": 0,
                    "callerMethod": "",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 21,
                    "methodName": "$_POST",
                    "originClassName": "",
                    "retClassName": "",
                    "signature": ".$_POST",
                    "source": True,
                    "sourceHash": "3506402",
                    "sourceValues": "root,",
                    "targetHash": "3506402",
                    "targetValues": "root"
                }, {
                    "args": "",
                    "callerClass": "",
                    "callerLineNumber": 0,
                    "callerMethod": "",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 22,
                    "methodName": "$_POST",
                    "originClassName": "",
                    "retClassName": "",
                    "signature": ".$_POST",
                    "source": True,
                    "sourceHash": "2430751009",
                    "sourceValues": "12312334,",
                    "targetHash": "2430751009",
                    "targetValues": "12312334"
                }, {
                    "args": "",
                    "callerClass": "",
                    "callerLineNumber": 0,
                    "callerMethod": "",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 23,
                    "methodName": "$_POST",
                    "originClassName": "",
                    "retClassName": "",
                    "signature": ".$_POST",
                    "source": True,
                    "sourceHash": "2487299128",
                    "sourceValues": "Submit,",
                    "targetHash": "2487299128",
                    "targetValues": "Submit"
                }, {
                    "args": "root",
                    "callerClass": "",
                    "callerLineNumber": 0,
                    "callerMethod": "",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 24,
                    "methodName": "",
                    "originClassName": "",
                    "retClassName": "String",
                    "signature": "",
                    "source": False,
                    "sourceHash": "3506402",
                    "sourceValues": "root,",
                    "targetHash": "3264164444,3264164444",
                    "targetValues": "User Name:root,User Name:root"
                }, {
                    "args": "User Name:root,\n",
                    "callerClass": "",
                    "callerLineNumber": 0,
                    "callerMethod": "",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 25,
                    "methodName": "",
                    "originClassName": "",
                    "retClassName": "String",
                    "signature": "",
                    "source": False,
                    "sourceHash": "3264164444,10",
                    "sourceValues": "User Name:root,\n,",
                    "targetHash": "2404849966,2404849966",
                    "targetValues": "User Name:root\n,User Name:root\n"
                }, {
                    "args": "User Name:root\n",
                    "callerClass": "",
                    "callerLineNumber": 53,
                    "callerMethod": "main",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 26,
                    "methodName": "fwrite",
                    "originClassName": "",
                    "retClassName": "",
                    "signature": ".fwrite",
                    "source": False,
                    "sourceHash": "2404849966",
                    "sourceValues": "User Name:root\n,",
                    "targetHash": "",
                    "targetValues": ""
                }, {
                    "args": "12312334",
                    "callerClass": "",
                    "callerLineNumber": 0,
                    "callerMethod": "",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 27,
                    "methodName": "",
                    "originClassName": "",
                    "retClassName": "String",
                    "signature": "",
                    "source": False,
                    "sourceHash": "2430751009",
                    "sourceValues": "12312334,",
                    "targetHash": "2573646592,2573646592",
                    "targetValues": "Password:12312334,Password:12312334"
                }, {
                    "args":
                    "Password:12312334,\n",
                    "callerClass":
                    "",
                    "callerLineNumber":
                    0,
                    "callerMethod":
                    "",
                    "className":
                    "",
                    "interfaces":
                    "[]",
                    "invokeId":
                    28,
                    "methodName":
                    "",
                    "originClassName":
                    "",
                    "retClassName":
                    "String",
                    "signature":
                    "",
                    "source":
                    False,
                    "sourceHash":
                    "2573646592,10",
                    "sourceValues":
                    "Password:12312334,\n,",
                    "targetHash":
                    "2473633034,2473633034",
                    "targetValues":
                    "Password:12312334\n,Password:12312334\n"
                }, {
                    "args": "Password:12312334\n",
                    "callerClass": "",
                    "callerLineNumber": 54,
                    "callerMethod": "main",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 29,
                    "methodName": "fwrite",
                    "originClassName": "",
                    "retClassName": "",
                    "signature": ".fwrite",
                    "source": False,
                    "sourceHash": "2473633034",
                    "sourceValues": "Password:12312334\n,",
                    "targetHash": "",
                    "targetValues": ""
                }, {
                    "args": "root",
                    "callerClass": "",
                    "callerLineNumber": 0,
                    "callerMethod": "",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 30,
                    "methodName": "",
                    "originClassName": "",
                    "retClassName": "String",
                    "signature": "",
                    "source": False,
                    "sourceHash": "3506402",
                    "sourceValues": "root,",
                    "targetHash": "34906116,34906116",
                    "targetValues": "\"root,\"root"
                }, {
                    "args": "\"root,\"",
                    "callerClass": "",
                    "callerLineNumber": 0,
                    "callerMethod": "",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 31,
                    "methodName": "",
                    "originClassName": "",
                    "retClassName": "String",
                    "signature": "",
                    "source": False,
                    "sourceHash": "34906116,34",
                    "sourceValues": "\"root,\",",
                    "targetHash": "1082089630,1082089630",
                    "targetValues": "\"root\",\"root\""
                }, {
                    "args": "12312334",
                    "callerClass": "",
                    "callerLineNumber": 0,
                    "callerMethod": "",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 32,
                    "methodName": "",
                    "originClassName": "",
                    "retClassName": "String",
                    "signature": "",
                    "source": False,
                    "sourceHash": "2430751009",
                    "sourceValues": "12312334,",
                    "targetHash": "1106841411,1106841411",
                    "targetValues": "\"12312334,\"12312334"
                }, {
                    "args": "\"12312334,\"",
                    "callerClass": "",
                    "callerLineNumber": 0,
                    "callerMethod": "",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 33,
                    "methodName": "",
                    "originClassName": "",
                    "retClassName": "String",
                    "signature": "",
                    "source": False,
                    "sourceHash": "1106841411,34",
                    "sourceValues": "\"12312334,\",",
                    "targetHash": "4247312703,4247312703",
                    "targetValues": "\"12312334\",\"12312334\""
                }, {
                    "args":
                    "",
                    "callerClass":
                    "",
                    "callerLineNumber":
                    61,
                    "callerMethod":
                    "",
                    "className":
                    "",
                    "interfaces":
                    "[]",
                    "invokeId":
                    34,
                    "methodName":
                    "ZEND_ROPE_END",
                    "originClassName":
                    "",
                    "retClassName":
                    "String",
                    "signature":
                    ".ZEND_ROPE_END",
                    "source":
                    False,
                    "sourceHash":
                    "3935959953,1082089630,1478523430,4247312703,1876301945",
                    "sourceValues":
                    "SELECT username, password FROM users WHERE username=(,\"root\",) and password=(,\"12312334\",) LIMIT 0,1,",
                    "targetHash":
                    "3553945957",
                    "targetValues":
                    "SELECT username, password FROM users WHERE username=(\"root\") and password=(\"12312334\") LIMIT 0,1"
                }, {
                    "args":
                    "SELECT username, password FROM users WHERE username=(\"root\") and password=(\"12312334\") LIMIT 0,1,\"12312334",
                    "callerClass": "",
                    "callerLineNumber": 62,
                    "callerMethod": "main",
                    "className": "",
                    "interfaces": "[]",
                    "invokeId": 35,
                    "methodName": "mysqli_query",
                    "originClassName": "",
                    "retClassName": "",
                    "signature": ".mysqli_query",
                    "source": False,
                    "sourceHash": "3553945957,1106841411",
                    "sourceValues":
                    "SELECT username, password FROM users WHERE username=(\"root\") and password=(\"12312334\") LIMIT 0,1,\"12312334,",
                    "targetHash": "",
                    "targetValues": ""
                }],
                "protocol":
                "HTTP/1.1",
                "replayRequest":
                False,
                "reqBody":
                "",
                "reqHeader":
                "",
                "resBody":
                "",
                "resHeader":
                "",
                "scheme":
                "http",
                "secure":
                False,
                "uri":
                "/Less-12/",
                "url":
                "http://127.0.0.1:8008"
            },
            "type": 36
        }
        method['detail']['agentId'] = self.agent_id
        data = gzipdata(method)
        response = self.client.post('http://testserver/api/v1/report/upload',
                                    data=data,
                                    HTTP_CONTENT_ENCODING='gzip',
                                    content_type='application/json',
                                    )
        assert response.status_code == 200
        res = MethodPool.objects.filter(agent_id=self.agent_id).all()
        assert len(res) == 1


    def test_agent_method_pool_from_go_agent(self):
        data = {
            "type": 36,
            "detail": {
                "agentId":
                4025,
                "disk":
                "",
                "memory":
                "",
                "cpu":
                "",
                "methodQueue":
                0,
                "replayQueue":
                0,
                "reqCount":
                0,
                "reportQueue":
                0,
                "packagePath":
                "",
                "packageSignature":
                "",
                "packageName":
                "",
                "packageAlgorithm":
                "",
                "uri":
                "/sqli1",
                "url":
                "http://localhost:9999/sqli123132123313132321123231",
                "protocol":
                "HTTP/1.1",
                "contextPath":
                "",
                "pool": [{
                    "invokeId":
                    40252101640145388,
                    "interfaces": [],
                    "targetHash":
                    ["824634910755", "824634910761", "0", "0", "0", "0"],
                    "targetValues":
                    "Level low     ",
                    "signature":
                    "go-agent/core/httpRequestCookie.Cookie(0xc00014e100, {0x8420f8, 0x5})\n",
                    "originClassName":
                    "http.(*Request)",
                    "sourceValues":
                    "Level ",
                    "methodName":
                    "Cookie",
                    "className":
                    "http.(*Request)",
                    "source":
                    True,
                    "callerLineNumber":
                    49,
                    "callerClass":
                    "github.com/govwa/util",
                    "args":
                    "[\"Level\"]",
                    "callerMethod":
                    "GetCookie(0xc00014e100, {0x8420f8, 0x5})\n",
                    "sourceHash": ["8659192"],
                    "retClassName":
                    "*http.Cookie "
                }, {
                    "invokeId":
                    40252101640145389,
                    "interfaces": [],
                    "targetHash": [
                        "824634288360", "824634288368", "824634288378",
                        "824634288384", "824634288396", "824634288400",
                        "824634288416", "0"
                    ],
                    "targetValues":
                    "root Aa@6447985 govwa localhost 3306 http://localhost 9999  ",
                    "signature":
                    "go-agent/core/jsonUnmarshal.Unmarshal({0xc000324200, 0xd9, 0x200}, {0x79e520, 0xc0001da580})\n",
                    "originClassName":
                    "fmt",
                    "sourceValues":
                    "",
                    "methodName":
                    "Sprintf",
                    "className":
                    "fmt",
                    "source":
                    True,
                    "callerLineNumber":
                    29,
                    "callerClass":
                    "github.com/govwa/util/config",
                    "args":
                    "[\"ewogICAgInVzZXIiOiAicm9vdCIsCiAgICAicGFzc3dvcmQiOiAiQWFANjQ0Nzk4NSIsCiAgICAiZGJuYW1lIjogImdvdndhIiwKICAgICJzcWxob3N0IjogImxvY2FsaG9zdCIsCiAgICAic3FscG9ydCI6ICIzMzA2IiwKICAgICJ3ZWJzZXJ2ZXIiOiAiaHR0cDovL2xvY2FsaG9zdCIsCiAgICAid2VicG9ydCI6ICI5OTk5IiwKCiAgICAic2Vzc2lvbmtleToiOiAiRzBWdzQ0NCIKfQ==\"]",
                    "callerMethod":
                    "LoadConfig()\n",
                    "sourceHash":
                    None,
                    "retClassName":
                    "*config.Config "
                }, {
                    "invokeId":
                    40252101640145390,
                    "interfaces": [],
                    "targetHash": ["824636572896"],
                    "targetValues":
                    "root:Aa@6447985@tcp(localhost:3306)/ ",
                    "signature":
                    "go-agent/core/fmtSprintf.Sprintf({0x84afe4, 0x11}, {0xc00032c4b8, 0x4, 0x4})\n",
                    "originClassName":
                    "fmt",
                    "sourceValues":
                    "%s:%s@tcp(%s:%s)/ root Aa@6447985 localhost 3306 ",
                    "methodName":
                    "Sprintf",
                    "className":
                    "fmt",
                    "source":
                    False,
                    "callerLineNumber":
                    18,
                    "callerClass":
                    "github.com/govwa/util/database",
                    "args":
                    "[\"%s:%s@tcp(%s:%s)/\",[\"root\",\"Aa@6447985\",\"localhost\",\"3306\"]]",
                    "callerMethod":
                    "Connect()\n",
                    "sourceHash": [
                        "8695780", "824634288360", "824634288368",
                        "824634288384", "824634288396"
                    ],
                    "retClassName":
                    "string "
                }, {
                    "invokeId":
                    40252101640145391,
                    "interfaces": [],
                    "targetHash": ["824636573472"],
                    "targetValues":
                    "root:Aa@6447985@tcp(localhost:3306)/govwa ",
                    "signature":
                    "go-agent/core/fmtSprintf.Sprintf({0x84c9df, 0x13}, {0xc00032c4f8, 0x5, 0x5})\n",
                    "originClassName":
                    "fmt",
                    "sourceValues":
                    "%s:%s@tcp(%s:%s)/%s root Aa@6447985 localhost 3306 govwa ",
                    "methodName":
                    "Sprintf",
                    "className":
                    "fmt",
                    "source":
                    False,
                    "callerLineNumber":
                    30,
                    "callerClass":
                    "github.com/govwa/util/database",
                    "args":
                    "[\"%s:%s@tcp(%s:%s)/%s\",[\"root\",\"Aa@6447985\",\"localhost\",\"3306\",\"govwa\"]]",
                    "callerMethod":
                    "Connect()\n",
                    "sourceHash": [
                        "8702431", "824634288360", "824634288368",
                        "824634288384", "824634288396", "824634288378"
                    ],
                    "retClassName":
                    "string "
                }, {
                    "invokeId":
                    40252101640145390,
                    "interfaces": [],
                    "targetHash":
                    ["824634910484", "824634910490", "0", "0", "0", "0"],
                    "targetValues":
                    "govwa MTY0MDE0NDg3NHxEdi1CQkFFQ180SUFBUkFCRUFBQVh2LUNBQU1HYzNSeWFXNW5EQThBRFdkdmRuZGhYM05sYzNOcGIyNEVZbTl2YkFJQ0FBRUdjM1J5YVc1bkRBY0FCWFZ1WVcxbEJuTjBjbWx1Wnd3SEFBVmhaRzFwYmdaemRISnBibWNNQkFBQ2FXUUdjM1J5YVc1bkRBTUFBVEU9fPfvm5eU0A5drQKDLDOgC_ffWcZue0sMf7EbJ7H5XzIj     ",
                    "signature":
                    "go-agent/core/httpRequestCookie.Cookie(0xc00014e100, {0x8424b8, 0x5})\n",
                    "originClassName":
                    "http.(*Request)",
                    "sourceValues":
                    "govwa ",
                    "methodName":
                    "Cookie",
                    "className":
                    "http.(*Request)",
                    "source":
                    True,
                    "callerLineNumber":
                    91,
                    "callerClass":
                    "github.com/gorilla/sessions.(*CookieStore)",
                    "args":
                    "[\"govwa\"]",
                    "callerMethod":
                    "New(0xc0000b6ce0, 0xc00014e100, {0x8424b8, 0x5})\n",
                    "sourceHash": ["8660152"],
                    "retClassName":
                    "*http.Cookie "
                }, {
                    "invokeId":
                    40252101640145391,
                    "interfaces": [],
                    "targetHash":
                    ["824634910748", "824634910752", "0", "0", "0", "0"],
                    "targetValues":
                    "Uid 1     ",
                    "signature":
                    "go-agent/core/httpRequestCookie.Cookie(0xc00014e100, {0x8413f6, 0x3})\n",
                    "originClassName":
                    "http.(*Request)",
                    "sourceValues":
                    "Uid ",
                    "methodName":
                    "Cookie",
                    "className":
                    "http.(*Request)",
                    "source":
                    True,
                    "callerLineNumber":
                    49,
                    "callerClass":
                    "github.com/govwa/util",
                    "args":
                    "[\"Uid\"]",
                    "callerMethod":
                    "GetCookie(0xc00014e100, {0x8413f6, 0x3})\n",
                    "sourceHash": ["8655862"],
                    "retClassName":
                    "*http.Cookie "
                }, {
                    "invokeId": 40252101640145392,
                    "interfaces": [],
                    "targetHash": ["824635081280"],
                    "targetValues":
                    "SELECT p.user_id, p.full_name, p.city, p.phone_number \n\t\t\t\t\t\t\t\tFROM Profile as p,Users as u \n\t\t\t\t\t\t\t\twhere p.user_id = u.id \n\t\t\t\t\t\t\t\tand u.id=1 ",
                    "signature":
                    "go-agent/core/fmtSprintf.Sprintf({0x86883b, 0x90}, {0xc00032c6c0, 0x1, 0x1})\n",
                    "originClassName": "fmt",
                    "sourceValues":
                    "SELECT p.user_id, p.full_name, p.city, p.phone_number \n\t\t\t\t\t\t\t\tFROM Profile as p,Users as u \n\t\t\t\t\t\t\t\twhere p.user_id = u.id \n\t\t\t\t\t\t\t\tand u.id=%s 1 ",
                    "methodName": "Sprintf",
                    "className": "fmt",
                    "source": False,
                    "callerLineNumber": 38,
                    "callerClass":
                    "github.com/govwa/vulnerability/sqli.(*Profile)",
                    "args":
                    "[\"SELECT p.user_id, p.full_name, p.city, p.phone_number \\n\\t\\t\\t\\t\\t\\t\\t\\tFROM Profile as p,Users as u \\n\\t\\t\\t\\t\\t\\t\\t\\twhere p.user_id = u.id \\n\\t\\t\\t\\t\\t\\t\\t\\tand u.id=%s\",[\"1\"]]",
                    "callerMethod":
                    "UnsafeQueryGetData(0xc0002925c0, {0xc000122820, 0x1})\n",
                    "sourceHash": ["8816699", "824634910752"],
                    "retClassName": "string "
                }, {
                    "invokeId": 40252101640145393,
                    "interfaces": [],
                    "targetHash": None,
                    "targetValues": "",
                    "signature":
                    "go-agent/core/sqlDBQuery.Query(0xc0001c0a90, {0xc00014c240, 0x8f}, {0x0, 0x0, 0x0})\n",
                    "originClassName": "sql.(*DB)",
                    "sourceValues":
                    "SELECT p.user_id, p.full_name, p.city, p.phone_number \n\t\t\t\t\t\t\t\tFROM Profile as p,Users as u \n\t\t\t\t\t\t\t\twhere p.user_id = u.id \n\t\t\t\t\t\t\t\tand u.id=1 ",
                    "methodName": "Query",
                    "className": "sql.(*DB)",
                    "source": False,
                    "callerLineNumber": 42,
                    "callerClass":
                    "github.com/govwa/vulnerability/sqli.(*Profile)",
                    "args":
                    "[\"SELECT p.user_id, p.full_name, p.city, p.phone_number \\n\\t\\t\\t\\t\\t\\t\\t\\tFROM Profile as p,Users as u \\n\\t\\t\\t\\t\\t\\t\\t\\twhere p.user_id = u.id \\n\\t\\t\\t\\t\\t\\t\\t\\tand u.id=1\",None]",
                    "callerMethod":
                    "UnsafeQueryGetData(0xc0002925c0, {0xc000122820, 0x1})\n",
                    "sourceHash": ["824635081280"],
                    "retClassName": "*sql.Rows *errors.errorString "
                }],
                "language":
                "GO",
                "clientIp":
                "[::1]:53457",
                "secure":
                False,
                "queryString":
                "",
                "replayRequest":
                False,
                "method":
                "GET",
                "reqHeader":
                "eyJBY2NlcHQiOlsidGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCxhcHBsaWNhdGlvbi9zaWduZWQtZXhjaGFuZ2U7dj1iMztxPTAuOSJdLCJBY2NlcHQtRW5jb2RpbmciOlsiZ3ppcCwgZGVmbGF0ZSwgYnIiXSwiQWNjZXB0LUxhbmd1YWdlIjpbInpoLUNOLHpoO3E9MC45LGVuLUdCO3E9MC44LGVuO3E9MC43LGVuLVVTO3E9MC42Il0sIkNvbm5lY3Rpb24iOlsia2VlcC1hbGl2ZSJdLCJDb29raWUiOlsiSG1fbHZ0XzY5YmUxNTIzNTFlNDc5YjhiNjRmNzdhOTM0NzAzYTU1PTE2Mzk3MjcwNjA7IGdvdndhPU1UWTBNREUwTkRnM05IeEVkaTFDUWtGRlExODBTVUZCVWtGQ1JVRkJRVmgyTFVOQlFVMUhZek5TZVdGWE5XNUVRVGhCUkZka2RtUnVaR2hZTTA1c1l6Tk9jR0l5TkVWWmJUbDJZa0ZKUTBGQlJVZGpNMUo1WVZjMWJrUkJZMEZDV0ZaMVdWY3hiRUp1VGpCamJXeDFXbmQzU0VGQlZtaGFSekZ3WW1kYWVtUklTbkJpYldOTlFrRkJRMkZYVVVkak0xSjVZVmMxYmtSQlRVRkJWRVU5ZlBmdm01ZVUwQTVkclFLRExET2dDX2ZmV2NadWUwc01mN0ViSjdINVh6SWo7IFVpZD0xOyBMZXZlbD1sb3ciXSwiUmVmZXJlciI6WyJodHRwOi8vbG9jYWxob3N0Ojk5OTkvc3FsaTEiXSwiU2VjLUNoLVVhIjpbIlwiIE5vdCBBO0JyYW5kXCI7dj1cIjk5XCIsIFwiQ2hyb21pdW1cIjt2PVwiOTZcIiwgXCJNaWNyb3NvZnQgRWRnZVwiO3Y9XCI5NlwiIl0sIlNlYy1DaC1VYS1Nb2JpbGUiOlsiPzAiXSwiU2VjLUNoLVVhLVBsYXRmb3JtIjpbIlwiV2luZG93c1wiIl0sIlNlYy1GZXRjaC1EZXN0IjpbImRvY3VtZW50Il0sIlNlYy1GZXRjaC1Nb2RlIjpbIm5hdmlnYXRlIl0sIlNlYy1GZXRjaC1TaXRlIjpbInNhbWUtb3JpZ2luIl0sIlNlYy1GZXRjaC1Vc2VyIjpbIj8xIl0sIlVwZ3JhZGUtSW5zZWN1cmUtUmVxdWVzdHMiOlsiMSJdLCJVc2VyLUFnZW50IjpbIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuMTEwIFNhZmFyaS81MzcuMzYgRWRnLzk2LjAuMTA1NC42MiJdfQ==",
                "reqBody":
                "",
                "resBody":
                "               \u003cp\u003eYour Profile :\u003c/p\u003e\n                    sql: converting argument $1 type: unsupported type []interface {}, a slice of interface \n\u003cpre\u003e\nUid     : 1\nName    : \nCity    :  \nNumber  :  \n\u003c/pre\u003e\n                \u003cdiv class=\"more-info\"\u003e\n                    \u003cspan\u003eMore Info :\u003c/span\u003e\n                    \u003ca target=\"_blank\" href=\"http://www.sqlinjection.net/union/\"\u003ehttp://www.sqlinjection.net/union/\u003c/a\u003e\n                    \u003ca target=\"_blank\" href=\"https://www.owasp.org/index.php/SQL_Injection\"\u003ehttps://www.owasp.org/index.php/SQL_Injection\u003c/a\u003e\n                \u003c/div\u003e\n            \u003c/div\u003e\n        \u003c/div\u003e\n    \u003c/div\u003e\n\u003c/div\u003e\n\n\u003c/div\u003e\n\n\n    \u003cfooter class=\"footer\"\u003e\n        \u003cdiv class=\"container\"\u003e\n          \u003cspan\u003e\u003ci class=\"fa fa-copyright\"\u003e\u003c/i\u003eNemosecurity\u003c/span\u003e\n        \u003c/div\u003e\n      \u003c/footer\u003e\n\u003c/div\u003e\n\n\u003c/body\u003e\n\n\u003c/html\u003e\n           \u003cli\u003e\u003ca href=\"idor1\"\u003eIDOR 1\u003c/a\u003e\u003c/li\u003e\n                            \u003cli\u003e\u003ca href=\"idor2\"\u003eIDOR 2\u003c/a\u003e\u003c/li\u003e\n                        \u003c/ul\u003e\n\n                   \n                    \u003cli\u003e\n                            \u003ca href=\"csa\"\u003e\n                                \u003ci class=\"fa fa-bug fa-lg\"\u003e\u003c/i\u003e Client Side Auth\n                            \u003c/a\u003e\n                        \u003c/li\u003e\n                    \u003cli style=\"height:35px\"\u003e\n                    \u003c/li\u003e\n                    \u003cli\u003e\n                            \u003ca href=\"setting\"\u003e\n                                \u003ci class=\"glyphicon glyphicon-cog fa-lg\"\u003e\u003c/i\u003e Setting\n                            \u003c/a\u003e\n                        \u003c/li\u003e\n                    \u003cli\u003e\n                            \u003ca href=\"logout\"\u003e\n                                \u003ci class=\"fa fa-sign-out fa-lg\"\u003e\u003c/i\u003e Logout\n                            \u003c/a\u003e\n                        \u003c/li\u003e\n                        \n                \u003c/ul\u003e\n            \u003c/div\u003e\n        \u003c/div\u003e\n    \u003c/div\u003e\n    \n\u003cdiv class=\"col-md-9\"\u003e\n    \u003cdiv class=\"panel panel-primary\"\u003e\n        \u003cdiv class=\"panel-heading\"\u003eSQL Injection Vulnerability\u003c/div\u003e\n        \u003cdiv class=\"panel-body\"\u003e\n            \u003cdiv class=\"pnl\"\u003e\n                \n                \u003cp\u003eThis should be safe\u003c/p\u003e\n ",
                "scheme":
                "",
                "resHeader":
                "e30=",
                "invokeId":
                0,
                "interfaces":
                None,
                "targetHash":
                None,
                "targetValues":
                "",
                "signature":
                "",
                "originClassName":
                "",
                "sourceValues":
                "",
                "methodName":
                "",
                "className":
                "",
                "source":
                False,
                "callerLineNumber":
                0,
                "callerClass":
                "",
                "args":
                "",
                "callerMethod":
                "",
                "sourceHash":
                None,
                "retClassName":
                "",
                "log":
                "",
                "apiData":
                None
            },
            "invoke_id": 40252101640145387
        }
        data['detail']['agentId'] = self.agent_id
        data = gzipdata(data)
        response = self.client.post('http://testserver/api/v1/report/upload',
                                    data=data,
                                    HTTP_CONTENT_ENCODING='gzip',
                                    content_type='application/json',
                                    )
        assert response.status_code == 200
        assert MethodPool.objects.filter(
            url="http://localhost:9999/sqli123132123313132321123231",
            agent_id=self.agent_id).exists()
    def test_agent_method_pool_gzip_test(self):
        data = {
            "type": 36,
            "detail": {
                "agentId":
                4025,
                "disk":
                "",
                "memory":
                "",
                "cpu":
                "",
                "methodQueue":
                0,
                "replayQueue":
                0,
                "reqCount":
                0,
                "reportQueue":
                0,
                "packagePath":
                "",
                "packageSignature":
                "",
                "packageName":
                "",
                "packageAlgorithm":
                "",
                "uri":
                "/sqli1",
                "url":
                "http://localhost:9999/sqli123132123313132321123231test",
                "protocol":
                "HTTP/1.1",
                "contextPath":
                "",
                "pool": [{
                    "invokeId":
                    40252101640145388,
                    "interfaces": [],
                    "targetHash":
                    ["824634910755", "824634910761", "0", "0", "0", "0"],
                    "targetValues":
                    "Level low     ",
                    "signature":
                    "go-agent/core/httpRequestCookie.Cookie(0xc00014e100, {0x8420f8, 0x5})\n",
                    "originClassName":
                    "http.(*Request)",
                    "sourceValues":
                    "Level ",
                    "methodName":
                    "Cookie",
                    "className":
                    "http.(*Request)",
                    "source":
                    True,
                    "callerLineNumber":
                    49,
                    "callerClass":
                    "github.com/govwa/util",
                    "args":
                    "[\"Level\"]",
                    "callerMethod":
                    "GetCookie(0xc00014e100, {0x8420f8, 0x5})\n",
                    "sourceHash": ["8659192"],
                    "retClassName":
                    "*http.Cookie "
                }, {
                    "invokeId":
                    40252101640145389,
                    "interfaces": [],
                    "targetHash": [
                        "824634288360", "824634288368", "824634288378",
                        "824634288384", "824634288396", "824634288400",
                        "824634288416", "0"
                    ],
                    "targetValues":
                    "root Aa@6447985 govwa localhost 3306 http://localhost 9999  ",
                    "signature":
                    "go-agent/core/jsonUnmarshal.Unmarshal({0xc000324200, 0xd9, 0x200}, {0x79e520, 0xc0001da580})\n",
                    "originClassName":
                    "fmt",
                    "sourceValues":
                    "",
                    "methodName":
                    "Sprintf",
                    "className":
                    "fmt",
                    "source":
                    True,
                    "callerLineNumber":
                    29,
                    "callerClass":
                    "github.com/govwa/util/config",
                    "args":
                    "[\"ewogICAgInVzZXIiOiAicm9vdCIsCiAgICAicGFzc3dvcmQiOiAiQWFANjQ0Nzk4NSIsCiAgICAiZGJuYW1lIjogImdvdndhIiwKICAgICJzcWxob3N0IjogImxvY2FsaG9zdCIsCiAgICAic3FscG9ydCI6ICIzMzA2IiwKICAgICJ3ZWJzZXJ2ZXIiOiAiaHR0cDovL2xvY2FsaG9zdCIsCiAgICAid2VicG9ydCI6ICI5OTk5IiwKCiAgICAic2Vzc2lvbmtleToiOiAiRzBWdzQ0NCIKfQ==\"]",
                    "callerMethod":
                    "LoadConfig()\n",
                    "sourceHash":
                    None,
                    "retClassName":
                    "*config.Config "
                }, {
                    "invokeId":
                    40252101640145390,
                    "interfaces": [],
                    "targetHash": ["824636572896"],
                    "targetValues":
                    "root:Aa@6447985@tcp(localhost:3306)/ ",
                    "signature":
                    "go-agent/core/fmtSprintf.Sprintf({0x84afe4, 0x11}, {0xc00032c4b8, 0x4, 0x4})\n",
                    "originClassName":
                    "fmt",
                    "sourceValues":
                    "%s:%s@tcp(%s:%s)/ root Aa@6447985 localhost 3306 ",
                    "methodName":
                    "Sprintf",
                    "className":
                    "fmt",
                    "source":
                    False,
                    "callerLineNumber":
                    18,
                    "callerClass":
                    "github.com/govwa/util/database",
                    "args":
                    "[\"%s:%s@tcp(%s:%s)/\",[\"root\",\"Aa@6447985\",\"localhost\",\"3306\"]]",
                    "callerMethod":
                    "Connect()\n",
                    "sourceHash": [
                        "8695780", "824634288360", "824634288368",
                        "824634288384", "824634288396"
                    ],
                    "retClassName":
                    "string "
                }, {
                    "invokeId":
                    40252101640145391,
                    "interfaces": [],
                    "targetHash": ["824636573472"],
                    "targetValues":
                    "root:Aa@6447985@tcp(localhost:3306)/govwa ",
                    "signature":
                    "go-agent/core/fmtSprintf.Sprintf({0x84c9df, 0x13}, {0xc00032c4f8, 0x5, 0x5})\n",
                    "originClassName":
                    "fmt",
                    "sourceValues":
                    "%s:%s@tcp(%s:%s)/%s root Aa@6447985 localhost 3306 govwa ",
                    "methodName":
                    "Sprintf",
                    "className":
                    "fmt",
                    "source":
                    False,
                    "callerLineNumber":
                    30,
                    "callerClass":
                    "github.com/govwa/util/database",
                    "args":
                    "[\"%s:%s@tcp(%s:%s)/%s\",[\"root\",\"Aa@6447985\",\"localhost\",\"3306\",\"govwa\"]]",
                    "callerMethod":
                    "Connect()\n",
                    "sourceHash": [
                        "8702431", "824634288360", "824634288368",
                        "824634288384", "824634288396", "824634288378"
                    ],
                    "retClassName":
                    "string "
                }, {
                    "invokeId":
                    40252101640145390,
                    "interfaces": [],
                    "targetHash":
                    ["824634910484", "824634910490", "0", "0", "0", "0"],
                    "targetValues":
                    "govwa MTY0MDE0NDg3NHxEdi1CQkFFQ180SUFBUkFCRUFBQVh2LUNBQU1HYzNSeWFXNW5EQThBRFdkdmRuZGhYM05sYzNOcGIyNEVZbTl2YkFJQ0FBRUdjM1J5YVc1bkRBY0FCWFZ1WVcxbEJuTjBjbWx1Wnd3SEFBVmhaRzFwYmdaemRISnBibWNNQkFBQ2FXUUdjM1J5YVc1bkRBTUFBVEU9fPfvm5eU0A5drQKDLDOgC_ffWcZue0sMf7EbJ7H5XzIj     ",
                    "signature":
                    "go-agent/core/httpRequestCookie.Cookie(0xc00014e100, {0x8424b8, 0x5})\n",
                    "originClassName":
                    "http.(*Request)",
                    "sourceValues":
                    "govwa ",
                    "methodName":
                    "Cookie",
                    "className":
                    "http.(*Request)",
                    "source":
                    True,
                    "callerLineNumber":
                    91,
                    "callerClass":
                    "github.com/gorilla/sessions.(*CookieStore)",
                    "args":
                    "[\"govwa\"]",
                    "callerMethod":
                    "New(0xc0000b6ce0, 0xc00014e100, {0x8424b8, 0x5})\n",
                    "sourceHash": ["8660152"],
                    "retClassName":
                    "*http.Cookie "
                }, {
                    "invokeId":
                    40252101640145391,
                    "interfaces": [],
                    "targetHash":
                    ["824634910748", "824634910752", "0", "0", "0", "0"],
                    "targetValues":
                    "Uid 1     ",
                    "signature":
                    "go-agent/core/httpRequestCookie.Cookie(0xc00014e100, {0x8413f6, 0x3})\n",
                    "originClassName":
                    "http.(*Request)",
                    "sourceValues":
                    "Uid ",
                    "methodName":
                    "Cookie",
                    "className":
                    "http.(*Request)",
                    "source":
                    True,
                    "callerLineNumber":
                    49,
                    "callerClass":
                    "github.com/govwa/util",
                    "args":
                    "[\"Uid\"]",
                    "callerMethod":
                    "GetCookie(0xc00014e100, {0x8413f6, 0x3})\n",
                    "sourceHash": ["8655862"],
                    "retClassName":
                    "*http.Cookie "
                }, {
                    "invokeId": 40252101640145392,
                    "interfaces": [],
                    "targetHash": ["824635081280"],
                    "targetValues":
                    "SELECT p.user_id, p.full_name, p.city, p.phone_number \n\t\t\t\t\t\t\t\tFROM Profile as p,Users as u \n\t\t\t\t\t\t\t\twhere p.user_id = u.id \n\t\t\t\t\t\t\t\tand u.id=1 ",
                    "signature":
                    "go-agent/core/fmtSprintf.Sprintf({0x86883b, 0x90}, {0xc00032c6c0, 0x1, 0x1})\n",
                    "originClassName": "fmt",
                    "sourceValues":
                    "SELECT p.user_id, p.full_name, p.city, p.phone_number \n\t\t\t\t\t\t\t\tFROM Profile as p,Users as u \n\t\t\t\t\t\t\t\twhere p.user_id = u.id \n\t\t\t\t\t\t\t\tand u.id=%s 1 ",
                    "methodName": "Sprintf",
                    "className": "fmt",
                    "source": False,
                    "callerLineNumber": 38,
                    "callerClass":
                    "github.com/govwa/vulnerability/sqli.(*Profile)",
                    "args":
                    "[\"SELECT p.user_id, p.full_name, p.city, p.phone_number \\n\\t\\t\\t\\t\\t\\t\\t\\tFROM Profile as p,Users as u \\n\\t\\t\\t\\t\\t\\t\\t\\twhere p.user_id = u.id \\n\\t\\t\\t\\t\\t\\t\\t\\tand u.id=%s\",[\"1\"]]",
                    "callerMethod":
                    "UnsafeQueryGetData(0xc0002925c0, {0xc000122820, 0x1})\n",
                    "sourceHash": ["8816699", "824634910752"],
                    "retClassName": "string "
                }, {
                    "invokeId": 40252101640145393,
                    "interfaces": [],
                    "targetHash": None,
                    "targetValues": "",
                    "signature":
                    "go-agent/core/sqlDBQuery.Query(0xc0001c0a90, {0xc00014c240, 0x8f}, {0x0, 0x0, 0x0})\n",
                    "originClassName": "sql.(*DB)",
                    "sourceValues":
                    "SELECT p.user_id, p.full_name, p.city, p.phone_number \n\t\t\t\t\t\t\t\tFROM Profile as p,Users as u \n\t\t\t\t\t\t\t\twhere p.user_id = u.id \n\t\t\t\t\t\t\t\tand u.id=1 ",
                    "methodName": "Query",
                    "className": "sql.(*DB)",
                    "source": False,
                    "callerLineNumber": 42,
                    "callerClass":
                    "github.com/govwa/vulnerability/sqli.(*Profile)",
                    "args":
                    "[\"SELECT p.user_id, p.full_name, p.city, p.phone_number \\n\\t\\t\\t\\t\\t\\t\\t\\tFROM Profile as p,Users as u \\n\\t\\t\\t\\t\\t\\t\\t\\twhere p.user_id = u.id \\n\\t\\t\\t\\t\\t\\t\\t\\tand u.id=1\",None]",
                    "callerMethod":
                    "UnsafeQueryGetData(0xc0002925c0, {0xc000122820, 0x1})\n",
                    "sourceHash": ["824635081280"],
                    "retClassName": "*sql.Rows *errors.errorString "
                }],
                "language":
                "GO",
                "clientIp":
                "[::1]:53457",
                "secure":
                False,
                "queryString":
                "",
                "replayRequest":
                False,
                "method":
                "GET",
                "reqHeader":
                "eyJBY2NlcHQiOlsidGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCxhcHBsaWNhdGlvbi9zaWduZWQtZXhjaGFuZ2U7dj1iMztxPTAuOSJdLCJBY2NlcHQtRW5jb2RpbmciOlsiZ3ppcCwgZGVmbGF0ZSwgYnIiXSwiQWNjZXB0LUxhbmd1YWdlIjpbInpoLUNOLHpoO3E9MC45LGVuLUdCO3E9MC44LGVuO3E9MC43LGVuLVVTO3E9MC42Il0sIkNvbm5lY3Rpb24iOlsia2VlcC1hbGl2ZSJdLCJDb29raWUiOlsiSG1fbHZ0XzY5YmUxNTIzNTFlNDc5YjhiNjRmNzdhOTM0NzAzYTU1PTE2Mzk3MjcwNjA7IGdvdndhPU1UWTBNREUwTkRnM05IeEVkaTFDUWtGRlExODBTVUZCVWtGQ1JVRkJRVmgyTFVOQlFVMUhZek5TZVdGWE5XNUVRVGhCUkZka2RtUnVaR2hZTTA1c1l6Tk9jR0l5TkVWWmJUbDJZa0ZKUTBGQlJVZGpNMUo1WVZjMWJrUkJZMEZDV0ZaMVdWY3hiRUp1VGpCamJXeDFXbmQzU0VGQlZtaGFSekZ3WW1kYWVtUklTbkJpYldOTlFrRkJRMkZYVVVkak0xSjVZVmMxYmtSQlRVRkJWRVU5ZlBmdm01ZVUwQTVkclFLRExET2dDX2ZmV2NadWUwc01mN0ViSjdINVh6SWo7IFVpZD0xOyBMZXZlbD1sb3ciXSwiUmVmZXJlciI6WyJodHRwOi8vbG9jYWxob3N0Ojk5OTkvc3FsaTEiXSwiU2VjLUNoLVVhIjpbIlwiIE5vdCBBO0JyYW5kXCI7dj1cIjk5XCIsIFwiQ2hyb21pdW1cIjt2PVwiOTZcIiwgXCJNaWNyb3NvZnQgRWRnZVwiO3Y9XCI5NlwiIl0sIlNlYy1DaC1VYS1Nb2JpbGUiOlsiPzAiXSwiU2VjLUNoLVVhLVBsYXRmb3JtIjpbIlwiV2luZG93c1wiIl0sIlNlYy1GZXRjaC1EZXN0IjpbImRvY3VtZW50Il0sIlNlYy1GZXRjaC1Nb2RlIjpbIm5hdmlnYXRlIl0sIlNlYy1GZXRjaC1TaXRlIjpbInNhbWUtb3JpZ2luIl0sIlNlYy1GZXRjaC1Vc2VyIjpbIj8xIl0sIlVwZ3JhZGUtSW5zZWN1cmUtUmVxdWVzdHMiOlsiMSJdLCJVc2VyLUFnZW50IjpbIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Ni4wLjQ2NjQuMTEwIFNhZmFyaS81MzcuMzYgRWRnLzk2LjAuMTA1NC42MiJdfQ==",
                "reqBody":
                "",
                "resBody":
                "               \u003cp\u003eYour Profile :\u003c/p\u003e\n                    sql: converting argument $1 type: unsupported type []interface {}, a slice of interface \n\u003cpre\u003e\nUid     : 1\nName    : \nCity    :  \nNumber  :  \n\u003c/pre\u003e\n                \u003cdiv class=\"more-info\"\u003e\n                    \u003cspan\u003eMore Info :\u003c/span\u003e\n                    \u003ca target=\"_blank\" href=\"http://www.sqlinjection.net/union/\"\u003ehttp://www.sqlinjection.net/union/\u003c/a\u003e\n                    \u003ca target=\"_blank\" href=\"https://www.owasp.org/index.php/SQL_Injection\"\u003ehttps://www.owasp.org/index.php/SQL_Injection\u003c/a\u003e\n                \u003c/div\u003e\n            \u003c/div\u003e\n        \u003c/div\u003e\n    \u003c/div\u003e\n\u003c/div\u003e\n\n\u003c/div\u003e\n\n\n    \u003cfooter class=\"footer\"\u003e\n        \u003cdiv class=\"container\"\u003e\n          \u003cspan\u003e\u003ci class=\"fa fa-copyright\"\u003e\u003c/i\u003eNemosecurity\u003c/span\u003e\n        \u003c/div\u003e\n      \u003c/footer\u003e\n\u003c/div\u003e\n\n\u003c/body\u003e\n\n\u003c/html\u003e\n           \u003cli\u003e\u003ca href=\"idor1\"\u003eIDOR 1\u003c/a\u003e\u003c/li\u003e\n                            \u003cli\u003e\u003ca href=\"idor2\"\u003eIDOR 2\u003c/a\u003e\u003c/li\u003e\n                        \u003c/ul\u003e\n\n                   \n                    \u003cli\u003e\n                            \u003ca href=\"csa\"\u003e\n                                \u003ci class=\"fa fa-bug fa-lg\"\u003e\u003c/i\u003e Client Side Auth\n                            \u003c/a\u003e\n                        \u003c/li\u003e\n                    \u003cli style=\"height:35px\"\u003e\n                    \u003c/li\u003e\n                    \u003cli\u003e\n                            \u003ca href=\"setting\"\u003e\n                                \u003ci class=\"glyphicon glyphicon-cog fa-lg\"\u003e\u003c/i\u003e Setting\n                            \u003c/a\u003e\n                        \u003c/li\u003e\n                    \u003cli\u003e\n                            \u003ca href=\"logout\"\u003e\n                                \u003ci class=\"fa fa-sign-out fa-lg\"\u003e\u003c/i\u003e Logout\n                            \u003c/a\u003e\n                        \u003c/li\u003e\n                        \n                \u003c/ul\u003e\n            \u003c/div\u003e\n        \u003c/div\u003e\n    \u003c/div\u003e\n    \n\u003cdiv class=\"col-md-9\"\u003e\n    \u003cdiv class=\"panel panel-primary\"\u003e\n        \u003cdiv class=\"panel-heading\"\u003eSQL Injection Vulnerability\u003c/div\u003e\n        \u003cdiv class=\"panel-body\"\u003e\n            \u003cdiv class=\"pnl\"\u003e\n                \n                \u003cp\u003eThis should be safe\u003c/p\u003e\n ",
                "scheme":
                "",
                "resHeader":
                "e30=",
                "invokeId":
                0,
                "interfaces":
                None,
                "targetHash":
                None,
                "targetValues":
                "",
                "signature":
                "",
                "originClassName":
                "",
                "sourceValues":
                "",
                "methodName":
                "",
                "className":
                "",
                "source":
                False,
                "callerLineNumber":
                0,
                "callerClass":
                "",
                "args":
                "",
                "callerMethod":
                "",
                "sourceHash":
                None,
                "retClassName":
                "",
                "log":
                "",
                "apiData":
                None
            },
            "invoke_id": 40252101640145387
        }
        data['detail']['agentId'] = self.agent_id
        testdata = '11231231321331232131231312233hwqeqqwe'
        data['detail'][
            'resHeader'] = "Q29udGVudC1UeXBlOmFwcGxpY2F0aW9uL2pzb24KWC1GcmFtZS1PcHRpb25zOkRFTlkKQ29udGVudC1MZW5ndGg6NjYKQ29udGVudC1lbmNvZGluZzpnemlwClgtQ29udGVudC1UeXBlLU9wdGlvbnM6bm9zbmlmZgpSZWZlcnJlci1Qb2xpY3k6c2FtZS1vcmlnaW4="
        data['version'] = 'v2'
        data['detail']['resBody'] = gzip_test_data = base64.b64encode(
            gzip.compress(bytes(
                testdata, encoding='utf-8'))).decode('raw_unicode_escape')
        data = gzipdata(data)
        response = self.client.post(
            'http://testserver/api/v1/report/upload',
            data=data,
            HTTP_CONTENT_ENCODING='gzip',
            content_type='application/json',
        )
        assert response.status_code == 200
        assert MethodPool.objects.filter(
            url="http://localhost:9999/sqli123132123313132321123231test",
            agent_id=self.agent_id).exists()
        assert not MethodPool.objects.filter(
            url="http://localhost:9999/sqli123132123313132321123231test",
            agent_id=self.agent_id,
            res_body=gzip_test_data).exists()

        assert MethodPool.objects.filter(
            url="http://localhost:9999/sqli123132123313132321123231test",
            agent_id=self.agent_id,
            res_body=testdata).exists()




    def test_agent_method_pool(self):
        data = {
            "detail": {
                "reqHeader":
                "QWNjZXB0OnRleHQvaHRtbCxhcHBsaWNhdGlvbi94aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3EKVXBncmFkZS1JbnNlY3VyZS1SZXF1ZXN0czoxClVzZXItQWdlbnQ6TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6OTguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC85OC4wCkNvbm5lY3Rpb246Y2xvc2UKSG9zdDoxMC4xODguMTM2LjE4Njo4OTYyCkFjY2VwdC1MYW5ndWFnZTp6aC1DTix6aDtxCkFjY2VwdC1FbmNvZGluZzpnemlwLCBkZWZsYXRlCmR0LXRyYWNlaWQ6Mzc1YWQyNTk1ZjFkNGQ4M2FhNzUwNmVkZjFmNWI4YTUtNTc5NjQwYWMxNzZhNGFmODgyNWNhNjg5MjM4OTM4MDUuNTguOTEuMApDb250ZW50LUxlbmd0aDo3NApDb250ZW50LVR5cGU6YXBwbGljYXRpb24vanNvbgo=",
                "agentId": 58,
                "scheme": "",
                "method": "POST",
                "contextPath": "/orderbase/queryOrderDetail",
                "pool": [],
                "secure": "",
                "uri": "/orderbase/queryOrderDetail",
                "url": "10.188.136.186:8962/orderbase/queryOrderDetail",
                "protocol": "HTTP/1.1",
                "resBody":
                "SFRUUC8xLjEgMjAwCngtdHJhY2UtaWQ6dHJpcG9yZGVyYmFzZS0wYWJjODhiYS00NTc5MDQtMjc1\nOTc1MDg1CmNvbnRlbnQtdHlwZTphcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0Cgp7InJldENvZGUi\nOjAsIm9yZGVySW5mbyI6eyJvcmRlck5vIjoiVDRpejE2bjl3MjdjM2U3MDE0ZmNkMjQ0NzA5N2Nj\nZGJhMjJkYjU0ODY4IiwidHJpcE5vIjoiVDRpejE2bjl3MjEyMTYyZjMzMDFjODE0NDgwOWExMGM5\nNzJjOWJhMDkwM2ExIiwiZGVtYW5kTm8iOiJUNGl6MTZuOXcyN2MzZTcwMTRmY2QyNDQ3MDk3Y2Nk\nYmEyMmRiNTQ4NjgiLCJjaXR5Q29kZSI6IjMxMDEwMCIsInN0YXR1cyI6ODAsInN1YlN0YXR1cyI6\nMCwicHJvZHVjdElkIjoiMSIsIm9yZGVyVHlwZSI6MiwiY2FyTGV2ZWwiOiIxMTAiLCJwYXNzZW5n\nZXJJZCI6IlAyZWEyYjg3ZGYwZTU0MGM5OTBhMGY3ZjAwYWNiZTE2OCIsImRyaXZlcklkIjoiRGM1\nZTIwZDIwYTVkZTQxODViZGQ0YjBjNTEzNDE2OTEyIiwib3JkZXJUaW1lIjoiMjAyMS0xMi0xMyAw\nMzoyNjo0MyIsIm9yaWdpbkNpdHlDb2RlIjoiMzEwMTAwIiwib3JpZ2luTG9jYXRpb24iOiIxMjEu\nODAyOTk5LDMxLjE0OTQ4NyIsIm9yaWdpbkFkZHJlc3MiOiLmnLrlnLrplYfnuqzkuIDot68xMDDl\nj7ciLCJvcmlnaW5Qb2kiOiLkuIrmtbfmtabkuJzlm73pmYXmnLrlnLox5Y+36Iiq56uZ5qW8Iiwi\nb3JpZ2luUG9pSWQiOiJCMDAxNTZUSjhPIiwiZGVzdGluYXRpb25DaXR5Q29kZSI6IjMxMDEwMCIs\nImRlc3RpbmF0aW9uTG9jYXRpb24iOiIxMjEuNDc1MTY0LDMxLjIyODgxNiIsImRlc3RpbmF0aW9u\nQWRkcmVzcyI6IuS6uuawkeWkp+mBkzIwMeWPtyIsImRlc3RpbmF0aW9uUG9pIjoi5LiK5rW35Y2a\n54mp6aaGIiwiZGVzdGluYXRpb25Qb2lJZCI6IkIwMDE1MzVCQkMiLCJwYXNzZW5nZXJUYWdzIjoi\nMSwwLDAsMiwwLDAsMCwwLDAsMCwwLDAsMCwxLDAsMCwwLDEsMCwxLDAiLCJkcml2ZXJUYWdzIjoi\nMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAiLCJkZWxldGVUYWciOjAsImNoYW5uZWxDb2RlIjoic2Fp\nYyIsImVzdGltYXRlSWQiOiIyMTEyMTM4YTY3MDcwZWE5N2U0YmZlODFlZDA0M2Q4NDg0NThjNjAy\nIiwiZXhwZW5JZCI6IjIxMTIxMzczZWFhMWU4N2VmNDQzYjQ4ZWI1OGVjYjc0ZmIzYzEzIiwiZGVt\nYW5kQXBwSWQiOiJzYWljX2NhciIsInN1cHBseUFwcElkIjoic2FpY19jYXJkIiwicGFzc2VuZ2Vy\nRXN0aW1hdGVGZWUiOjI1Mzg5LCJwYXNzZW5nZXJQYXlhYmxlRmVlIjoxODAwLCJwYXNzZW5nZXJQ\nYXltZW50RmVlIjoxODAwLCJkcml2ZXJSZWNlaXZlZEZlZSI6MTI1MCwidXBkYXRlVGltZSI6IjIw\nMjEtMTItMTMgMDM6Mjc6MDMiLCJjcmVhdGVUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNjo0NyIsImNh\nclVzZVRpbWUiOiIyMDIxLTEyLTEzIDA0OjMxOjQyIiwiaXNSZWYiOjAsInBheUJ5UGxhdGZvcm1G\nbGFnIjowLCJyYXRlRmxhZyI6MCwiaXNDYW5jZWwiOjAsImNhclVzZVR5cGUiOjEsImNhclVzZUR1\ncmF0aW9uIjowLCJjYXJVc2VTY2VuZSI6MCwicGFydGl0aW9uQ291bnQiOjAsInBhcnRpdGlvbklu\nZGV4IjowLCJkaXNwYXRjaE1vZGUiOjIsImVzdGltYXRlRHVyYXRpb24iOjAsImRhdGFTb3VyY2Ui\nOjAsImNhclNlcnZpY2UiOjEsInNpbXVsUmluZ0NhckxldmVsIjoiMTEwIiwidHJpcE1vZGUiOjAs\nInBheU9yZGVySWQiOiIyMDIxMTIxMzAzMjY1MzM2MDVhZTljZTJmMjQwM2E4MzAxYmNmMjEyMDQ5\nZDkxIiwib3JkZXJDcm93ZCI6MCwib3JkZXJMYXllciI6MCwic2NoZWR1bGVUeXBlIjowLCJleHRy\nYUludDEiOjAsImV4dHJhSW50MiI6MCwiZXh0cmFJbnQzIjowLCJleHRyYUludDQiOjAsImV4dHJh\nSW50NSI6MCwiZXN0aW1hdGVEaXN0YW5jZSI6MCwiZW50VHlwZSI6MCwicGF5bWVudENvbmZpcm1G\nbGFnIjowLCJwYXNzZW5nZXJTdXJ2ZXlGbGFnIjowLCJjaGFuZ2VUcmlwRmxhZyI6MCwib3JpZ2lu\nU3RhdGlvbkNvZGUiOiIwIiwiZGVzdGluYXRpb25TdGF0aW9uQ29kZSI6IjAiLCJwbGF0Zm9ybU1l\nc3NhZ2VGZWUiOjE5OSwiZGVzdGluYXRpb25UeXBlIjowLCJyZUNhbGxGbGFnIjowfSwiZHJpdmVy\nSW5mbyI6eyJvcmRlck5vIjoiVDRpejE2bjl3MjdjM2U3MDE0ZmNkMjQ0NzA5N2NjZGJhMjJkYjU0\nODY4IiwidHJpcE5vIjoiVDRpejE2bjl3MjEyMTYyZjMzMDFjODE0NDgwOWExMGM5NzJjOWJhMDkw\nM2ExIiwiZHJpdmVySWQiOiJEYzVlMjBkMjBhNWRlNDE4NWJkZDRiMGM1MTM0MTY5MTIiLCJkcml2\nZXJHcm91cHMiOiI0MiwzOTIiLCJkcml2ZXJOYW1lIjoi6YK55biI5YKFIiwiZHJpdmVyQXZhdGFy\nIjoiaHR0cHM6Ly9pb3QtdGVzdC1wZXJmb3JtYW5jZS5vc3MtY24taGFuZ3pob3UuYWxpeXVuY3Mu\nY29tL2ltYWdlcy9fYWxpXzRmYjQxNDJiMGQxZjQxNDM5MGUzZjk4ZWJhMDBiZTkzP0V4cGlyZXM9\nMzI1MDE5MjMyMDAmT1NTQWNjZXNzS2V5SWQ9TFRBSTRHMTVFSHRyUGI0YVZ1RVF4NVN1JlNpZ25h\ndHVyZT1LaGpQcGFoNDhpR2tOUGpjUzlwYlolMkZDOGlHRSUzRCIsImRyaXZlckFwcFZlcnNpb24i\nOiIzLjAuMCIsImRyaXZlclBsYXRmb3JtIjoiYW5kcm9pZCIsImRyaXZlclJhdGVTY29yZSI6NDQ5\nLCJkcml2ZXJEaXNwbGF5U2NvcmUiOjQ1MCwiZHJpdmVyVG90YWxEaXNwYXRjaE9yZGVyQ291bnQi\nOjE4MjIsInZlaGljbGVWaW4iOiJWSU40MTIyNDk2MzE4NjE2MSIsInZlaGljbGVObyI6Iua1izIx\nMDI1NTgiLCJ2ZWhpY2xlQ29sb3IiOiLnmb3oibIiLCJ2ZWhpY2xlQnJhbmQiOiLliKvlhYsiLCJ2\nZWhpY2xlTW9kZWwiOiJHTDYiLCJieXdheUFkZHJlc3MiOiLmuqfpmLPot682MTHlj7cxOTMz6ICB\n5Zy65Z2KMuWPt+alvCIsImFjdHVhbENhckxldmVsIjoiMTEwIiwidXBkYXRlVGltZSI6IjIwMjEt\nMTItMTMgMDM6Mjc6MDMiLCJjcmVhdGVUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNjo0NyIsInJld2Fy\nZEFtb3VudCI6MCwicHVuaXNoQW1vdW50IjowLCJwaWNrdXBFdGEiOjAsInBpY2t1cEVkYSI6MCwi\naXNEaXNwYXRjaGVkIjowLCJpc0ZyZWVEaXNwYXRjaGVkIjowLCJkcml2ZXJNb2JpbGUiOiIxMTIz\nMTAxMDgzNyIsImRyaXZlclNldHRsZW1lbnRNb2RlIjoxLCJkcml2ZXJDb21wbGV0ZU9yZGVyQ291\nbnQiOjg4NSwibGFzdFJlbGF5RXRhIjowLCJsYXN0UmVsYXlFZGEiOjAsImRyaXZlckFwcENhcGFj\naXR5IjoiMSwxLDEiLCJkcml2ZXJUcmFuc3BvcnRUeXBlIjoiMSIsImRyaXZlckFjdGl2aXR5UmV3\nYXJkIjowLCJkcml2ZXJMZXZlbElkIjoxLCJkcml2ZXJMZXZlbE5hbWUiOiLpnZLpk5wiLCJkcml2\nZXJFc3RpbWF0ZUZlZSI6MCwiZHJpdmVyQ29tcGxldGVPcmRlclNob3dDb3VudCI6MCwiZHJpdmVy\nQ29tcGxldGVEYWlseVNob3dDb3VudCI6MCwidmVoaWNsZVNlYXROdW0iOjB9LCJwYXNzZW5nZXJJ\nbmZvIjp7Im9yZGVyTm8iOiJUNGl6MTZuOXcyN2MzZTcwMTRmY2QyNDQ3MDk3Y2NkYmEyMmRiNTQ4\nNjgiLCJ0cmlwTm8iOiJUNGl6MTZuOXcyMTIxNjJmMzMwMWM4MTQ0ODA5YTEwYzk3MmM5YmEwOTAz\nYTEiLCJwYXNzZW5nZXJOYW1lIjoiMTEzKioqKjA4MzciLCJwYXNzZW5nZXJSYXRlU2NvcmUiOjQ2\nNiwicGFzc2VuZ2VyRGlzcGxheVNjb3JlIjo1LCJwYXNzZW5nZXJUb3RhbERpc3BhdGNoT3JkZXJD\nb3VudCI6NCwicGFzc2VuZ2VyQXBwVmVyc2lvbiI6IjMuMC4wIiwicGFzc2VuZ2VyUGxhdGZvcm0i\nOiJhbmRyb2lkIiwiZW50ZXJwcmlzZUlkIjowLCJlbnRlcnByaXNlUnVsZUlkIjowLCJhdXRvU2Vy\ndmljZUNvZGUiOiIwIiwiZW50ZXJwcmlzZU5lZWRSZW1hcmsiOjAsImVudGVycHJpc2VFbXBsb3ll\nZUlkIjoiMCIsImVudGVycHJpc2VBbW91bnQiOjAsInVwZGF0ZVRpbWUiOiIyMDIxLTEyLTEzIDAz\nOjI3OjAzIiwiY3JlYXRlVGltZSI6IjIwMjEtMTItMTMgMDM6MjY6NDciLCJwYXNzZW5nZXJJZCI6\nIlAyZWEyYjg3ZGYwZTU0MGM5OTBhMGY3ZjAwYWNiZTE2OCIsInBhc3Nlbmdlck1vYmlsZSI6IjEx\nMzMxMDEwODM3IiwiZmxpZ2h0Tm8iOiJLTjU5NTUiLCJmbGlnaHREZXAiOiJQS1giLCJmbGlnaHRB\ncnIiOiJTSEEiLCJmbGlnaHREYXRlIjoiMjAyMS0xMi0xMyAwMDowMDowMCIsImV4cFRpbWUiOjMw\nLCJvcmlnaW5hbEFwcG9pbnRtZW50VGltZSI6IjIwMjEtMTItMTMgMDQ6MzE6NDIiLCJpc0Rpc3Bh\ndGNoZWQiOiIwIiwiZ3Vlc3RDb3VudCI6MSwiZW50ZXJwcmlzZURpc2NvdW50IjoiMCIsImVudGVy\ncHJpc2VDb3N0Y2VudGVyIjowLCJlbnRlcnByaXNlQ29zdGNlbnRlck5hbWUiOiIwIiwiZW50ZXJw\ncmlzZUZyb3plblJhdGUiOiIwIiwicGF5TW9kZSI6MCwicGFzc2VuZ2VyU2V0dGxlbWVudE1vZGUi\nOjAsImZvbnRQbGFjYXJkIjoiIzRmNzBiZCIsInJ1bGVTbmFwU2hvdElkIjowLCJlbnRlcnByaXNl\nRGVwdElkIjowLCJhY3R1YWxQYXlNb2RlIjoxLCJwYXNzZW5nZXJDYXRlZ29yeSI6MCwib3BlcmF0\nb3JCeSI6MiwiZWdnRGlzY291bnQiOjAsImVnZ01heEFtb3VudCI6MCwiZWdnRmxhZyI6MCwidGF4\naURpc3BhdGNoRmVlIjowLCJlbnRlcnByaXNlQ2F0ZWdvcnkiOjAsInBhc3NlbmdlckFwcENhcGFj\naXR5IjoiMSwxLDEiLCJwYXNzZW5nZXJWYWx1YXRpb25Nb2RlIjoyLCJiZWxvbmdJZCI6MCwiYmVs\nb25nVHlwZSI6MCwidGVtcFJpc2VSYXRlIjowLCJ0ZW1wUmlzZUxpbWl0IjowLCJ0ZW1wUmlzZUZl\nZSI6MCwidGVtcFJpc2VUeXBlIjowLCJkaXNwYXRjaFJpc2VGZWUiOjAsImhvbGlkYXlSaXNlRmVl\nIjowLCJwYXNzZW5nZXJHZW5kZXIiOjB9LCJjYW5jZWxJbmZvIjp7ImNhbmNlbEJ5IjowLCJjYW5j\nZWxQYXllciI6MCwiY2FuY2VsRHV0eSI6MCwib3BlcmF0b3JCeSI6MCwib3JkZXJDb25maXJtRmxh\nZyI6MCwiZHV0eVNjZW5lIjowLCJ3b3Jrc2hlZXRUeXBlIjowLCJleHRDYW5jZWxEdXR5IjowLCJl\neHRDYW5jZWxGZWUiOjAsImV4dENhbmNlbER1dHlGcmVlIjowfSwiZmVlSW5mbyI6W3sib3JkZXJO\nbyI6IlQ0aXoxNm45dzI3YzNlNzAxNGZjZDI0NDcwOTdjY2RiYTIyZGI1NDg2OCIsImJhc2VGZWUi\nOjE4MDAsImV4dHJhRmVlIjowLCJ0b3RhbEZlZSI6MTgwMCwiZml4ZWRQcmljZSI6MCwiZHVyYXRp\nb24iOjEsImR1cmF0aW9uRmVlIjowLCJkaXN0YW5jZSI6MCwiZGlzdGFuY2VGZWUiOjAsIm1pbkZl\nZSI6MTcwMCwicGFya0ZlZSI6MCwid2FpdEZlZSI6MCwiYnJpZGdlRmVlIjowLCJjbGVhckZlZSI6\nMCwibG9uZ0Rpc3RhbmNlRmVlIjowLCJsb25nRGlzdGFuY2UiOjAsImNyb3NzQ2l0eUZlZSI6MCwi\nZGlzcGF0Y2hGZWUiOjAsIm5pZ2h0RmVlIjowLCJvdmVydGltZUZlZSI6MCwib3ZlcnRpbWUiOjAs\nImNhbmNlbEZlZSI6MCwiZmVlVHlwZSI6MSwidXBkYXRlVGltZSI6IjIwMjEtMTItMTMgMDM6MjY6\nNTMiLCJjcmVhdGVUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNjo1MyIsImFkanVzdEZlZSI6MCwiY291\ncG9uVHlwZSI6MCwiY291cG9uQW1vdW50IjowLCJwYXJ0aXRpb25JbmRleCI6MCwicGxhY2FyZEZl\nZSI6MCwib3RoZXJGZWUiOjAsInBsYXRmb3JtTWVzc2FnZUZlZSI6MCwicGFzc2VuZ2VyQ29uZmly\nbSI6MSwiYmFzZVRpbWUiOjEsImJhc2VNaWxlYWdlIjoxMDAwLCJleHRyYURpc3RhbmNlIjowLCJl\neHRyYUR1cmF0aW9uIjowLCJ2YWx1YXRpb25Nb2RlIjoyLCJsZXNzVGhhblN0YXJ0RmVlIjoxLCJ3\nYWl0VGltZSI6MCwiY291cG9uVmFsdWUiOjAsImNoZWFwQW1vdW50IjowLCJjaG9vc2VEcml2ZXJG\nZWUiOjAsImNvbW1pc3Npb25GZWUiOjAsImVudFNlcnZpY2VGZWUiOjAsInRlbXBSaXNlRmVlIjow\nLCJmZWVTdWJUeXBlIjowLCJwaWNrdXBFdGEiOjAsInBpY2t1cEVkYSI6MCwibG93U3BlZWREdXJh\ndGlvbiI6MCwibG93U3BlZWRGZWUiOjAsImRpc3RhbmNlQWxsb3dhbmNlRmVlIjowLCJ0YXhpRGlz\ncGF0Y2hGZWUiOjAsImZ1ZWxGZWUiOjAsInByaWNlSW5mbyI6IntcInRpbWVSYW5nZUZlZUluZm9c\nIjogW3tcIml0ZW1zXCI6IFt7XCJmZWVcIjogMTcwMCwgXCJlbmRUaW1lXCI6IFwiMTA6MzU6MDBc\nIiwgXCJiZWdpblRpbWVcIjogXCIwMDowMDowMFwiLCBcImZyZWVDb3VudFwiOiAwLCBcInRvdGFs\nQ291bnRcIjogMH1dLCBcImZlZVR5cGVcIjogXCJzdGFydEZlZVwifSwge1wiaXRlbXNcIjogW3tc\nImZlZVwiOiAwLCBcImVuZFRpbWVcIjogXCIxMTowMDowMFwiLCBcImJlZ2luVGltZVwiOiBcIjAw\nOjAwOjAwXCIsIFwiZnJlZUNvdW50XCI6IDEsIFwidG90YWxDb3VudFwiOiAxfV0sIFwiZmVlVHlw\nZVwiOiBcImR1cmF0aW9uRmVlXCJ9LCB7XCJmZWVUeXBlXCI6IFwiZGlzdGFuY2VGZWVcIn0sIHtc\nImZlZVR5cGVcIjogXCJsb25nRGlzdGFuY2VGZWVcIn1dfSIsImRpc3BhdGNoUmlzZUZlZSI6MCwi\naG9saWRheVJpc2VGZWUiOjEwMCwidGF4aUZlZSI6MH0seyJvcmRlck5vIjoiVDRpejE2bjl3Mjdj\nM2U3MDE0ZmNkMjQ0NzA5N2NjZGJhMjJkYjU0ODY4IiwiYmFzZUZlZSI6MCwiZXh0cmFGZWUiOjAs\nInRvdGFsRmVlIjoxODAwLCJmaXhlZFByaWNlIjowLCJkdXJhdGlvbiI6MCwiZHVyYXRpb25GZWUi\nOjAsImRpc3RhbmNlIjowLCJkaXN0YW5jZUZlZSI6MCwibWluRmVlIjowLCJwYXJrRmVlIjowLCJ3\nYWl0RmVlIjowLCJicmlkZ2VGZWUiOjAsImNsZWFyRmVlIjowLCJsb25nRGlzdGFuY2VGZWUiOjAs\nImxvbmdEaXN0YW5jZSI6MCwiY3Jvc3NDaXR5RmVlIjowLCJkaXNwYXRjaEZlZSI6MCwibmlnaHRG\nZWUiOjAsIm92ZXJ0aW1lRmVlIjowLCJvdmVydGltZSI6MCwiY2FuY2VsRmVlIjowLCJmZWVUeXBl\nIjoyLCJ1cGRhdGVUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNzowMyIsImNyZWF0ZVRpbWUiOiIyMDIx\nLTEyLTEzIDAzOjI3OjAzIiwiYWRqdXN0RmVlIjowLCJjb3Vwb25UeXBlIjowLCJjb3Vwb25BbW91\nbnQiOjAsInBhcnRpdGlvbkluZGV4IjowLCJwbGFjYXJkRmVlIjowLCJvdGhlckZlZSI6MCwicGF5\nbWVudFJlcXVlc3RJZCI6IjIxMTIxMzhhNjcwNzBlYTk3ZTRiZmU4MWVkMDQzZDg0ODQ1OGM2MDIi\nLCJwbGF0Zm9ybU1lc3NhZ2VGZWUiOjAsInBhc3NlbmdlckNvbmZpcm0iOjAsImJhc2VUaW1lIjow\nLCJiYXNlTWlsZWFnZSI6MCwiZXh0cmFEaXN0YW5jZSI6MCwiZXh0cmFEdXJhdGlvbiI6MCwidmFs\ndWF0aW9uTW9kZSI6MSwibGVzc1RoYW5TdGFydEZlZSI6MCwid2FpdFRpbWUiOjAsImNvdXBvblZh\nbHVlIjowLCJjaGVhcEFtb3VudCI6MCwiY2hvb3NlRHJpdmVyRmVlIjowLCJjb21taXNzaW9uRmVl\nIjowLCJlbnRTZXJ2aWNlRmVlIjowLCJ0ZW1wUmlzZUZlZSI6MCwiZmVlU3ViVHlwZSI6MCwicGlj\na3VwRXRhIjowLCJwaWNrdXBFZGEiOjAsImxvd1NwZWVkRHVyYXRpb24iOjAsImxvd1NwZWVkRmVl\nIjowLCJkaXN0YW5jZUFsbG93YW5jZUZlZSI6MCwidGF4aURpc3BhdGNoRmVlIjowLCJmdWVsRmVl\nIjowLCJkaXNwYXRjaFJpc2VGZWUiOjAsImhvbGlkYXlSaXNlRmVlIjowLCJ0YXhpRmVlIjowfSx7\nIm9yZGVyTm8iOiJUNGl6MTZuOXcyN2MzZTcwMTRmY2QyNDQ3MDk3Y2NkYmEyMmRiNTQ4NjgiLCJi\nYXNlRmVlIjoxMjUwLCJleHRyYUZlZSI6MCwidG90YWxGZWUiOjEyNTAsImZpeGVkUHJpY2UiOjAs\nImR1cmF0aW9uIjoxLCJkdXJhdGlvbkZlZSI6MCwiZGlzdGFuY2UiOjAsImRpc3RhbmNlRmVlIjow\nLCJtaW5GZWUiOjEyMDAsInBhcmtGZWUiOjAsIndhaXRGZWUiOjAsImJyaWRnZUZlZSI6MCwiY2xl\nYXJGZWUiOjAsImxvbmdEaXN0YW5jZUZlZSI6MCwibG9uZ0Rpc3RhbmNlIjowLCJjcm9zc0NpdHlG\nZWUiOjAsImRpc3BhdGNoRmVlIjowLCJuaWdodEZlZSI6MCwib3ZlcnRpbWVGZWUiOjAsIm92ZXJ0\naW1lIjowLCJjYW5jZWxGZWUiOjAsImZlZVR5cGUiOjMsInVwZGF0ZVRpbWUiOiIyMDIxLTEyLTEz\nIDAzOjI2OjUzIiwiY3JlYXRlVGltZSI6IjIwMjEtMTItMTMgMDM6MjY6NTMiLCJhZGp1c3RGZWUi\nOjAsImNvdXBvblR5cGUiOjAsImNvdXBvbkFtb3VudCI6MCwicGFydGl0aW9uSW5kZXgiOjAsInBs\nYWNhcmRGZWUiOjAsIm90aGVyRmVlIjowLCJwbGF0Zm9ybU1lc3NhZ2VGZWUiOjUwLCJwYXNzZW5n\nZXJDb25maXJtIjowLCJiYXNlVGltZSI6MTAsImJhc2VNaWxlYWdlIjozMDAwLCJleHRyYURpc3Rh\nbmNlIjowLCJleHRyYUR1cmF0aW9uIjowLCJ2YWx1YXRpb25Nb2RlIjoyLCJsZXNzVGhhblN0YXJ0\nRmVlIjoxLCJ3YWl0VGltZSI6MCwiY291cG9uVmFsdWUiOjAsImNoZWFwQW1vdW50IjowLCJjaG9v\nc2VEcml2ZXJGZWUiOjAsImNvbW1pc3Npb25GZWUiOjAsImVudFNlcnZpY2VGZWUiOjAsInRlbXBS\naXNlRmVlIjowLCJmZWVTdWJUeXBlIjowLCJwaWNrdXBFdGEiOjAsInBpY2t1cEVkYSI6MCwibG93\nU3BlZWREdXJhdGlvbiI6MCwibG93U3BlZWRGZWUiOjAsImRpc3RhbmNlQWxsb3dhbmNlRmVlIjow\nLCJ0YXhpRGlzcGF0Y2hGZWUiOjAsImZ1ZWxGZWUiOjAsInByaWNlSW5mbyI6IntcInRpbWVSYW5n\nZUZlZUluZm9cIjogW3tcIml0ZW1zXCI6IFt7XCJmZWVcIjogMTIwMCwgXCJlbmRUaW1lXCI6IFwi\nMTY6MDA6MDBcIiwgXCJiZWdpblRpbWVcIjogXCIwMDowMDowMFwiLCBcImZyZWVDb3VudFwiOiAw\nLCBcInRvdGFsQ291bnRcIjogMH1dLCBcImZlZVR5cGVcIjogXCJzdGFydEZlZVwifSwge1wiaXRl\nbXNcIjogW3tcImZlZVwiOiAwLCBcImVuZFRpbWVcIjogXCIxNjowMDowMFwiLCBcImJlZ2luVGlt\nZVwiOiBcIjAwOjAwOjAwXCIsIFwiZnJlZUNvdW50XCI6IDEsIFwidG90YWxDb3VudFwiOiAxfV0s\nIFwiZmVlVHlwZVwiOiBcImR1cmF0aW9uRmVlXCJ9LCB7XCJmZWVUeXBlXCI6IFwiZGlzdGFuY2VG\nZWVcIn0sIHtcImZlZVR5cGVcIjogXCJsb25nRGlzdGFuY2VGZWVcIn1dfSIsImRpc3BhdGNoUmlz\nZUZlZSI6MCwiaG9saWRheVJpc2VGZWUiOjEwMCwidGF4aUZlZSI6MH0seyJvcmRlck5vIjoiVDRp\nejE2bjl3MjdjM2U3MDE0ZmNkMjQ0NzA5N2NjZGJhMjJkYjU0ODY4IiwiYmFzZUZlZSI6MjUzODks\nImV4dHJhRmVlIjowLCJ0b3RhbEZlZSI6MjUzODksImZpeGVkUHJpY2UiOjAsImR1cmF0aW9uIjoy\nNjc5LCJkdXJhdGlvbkZlZSI6MzcxMCwiZGlzdGFuY2UiOjQ0NjUwLCJkaXN0YW5jZUZlZSI6MTU3\nMTQsIm1pbkZlZSI6MTcwMCwicGFya0ZlZSI6MCwid2FpdEZlZSI6MCwiYnJpZGdlRmVlIjowLCJj\nbGVhckZlZSI6MCwibG9uZ0Rpc3RhbmNlRmVlIjo0MTY1LCJsb25nRGlzdGFuY2UiOjQxNjUwLCJj\ncm9zc0NpdHlGZWUiOjAsImRpc3BhdGNoRmVlIjowLCJuaWdodEZlZSI6MCwib3ZlcnRpbWVGZWUi\nOjAsIm92ZXJ0aW1lIjowLCJjYW5jZWxGZWUiOjAsImZlZVR5cGUiOjcsInVwZGF0ZVRpbWUiOiIy\nMDIxLTEyLTEzIDAzOjI2OjQ3IiwiY3JlYXRlVGltZSI6IjIwMjEtMTItMTMgMDM6MjY6NDciLCJh\nZGp1c3RGZWUiOjAsImNvdXBvblR5cGUiOjAsImNvdXBvbkFtb3VudCI6MCwicGFydGl0aW9uSW5k\nZXgiOjAsInBsYWNhcmRGZWUiOjAsIm90aGVyRmVlIjowLCJwbGF0Zm9ybU1lc3NhZ2VGZWUiOjAs\nInBhc3NlbmdlckNvbmZpcm0iOjAsImJhc2VUaW1lIjoxLCJiYXNlTWlsZWFnZSI6MTAwMCwiZXh0\ncmFEaXN0YW5jZSI6NDM2NTAsImV4dHJhRHVyYXRpb24iOjI2MTksInZhbHVhdGlvbk1vZGUiOjIs\nImxlc3NUaGFuU3RhcnRGZWUiOjIsIndhaXRUaW1lIjowLCJjb3Vwb25WYWx1ZSI6MCwiY2hlYXBB\nbW91bnQiOjAsImNob29zZURyaXZlckZlZSI6MCwiY29tbWlzc2lvbkZlZSI6MCwiZW50U2Vydmlj\nZUZlZSI6MCwidGVtcFJpc2VGZWUiOjAsImZlZVN1YlR5cGUiOjEsInBpY2t1cEV0YSI6MCwicGlj\na3VwRWRhIjowLCJlc3RpbWF0ZUlkIjoiMjExMjEzOGE2NzA3MGVhOTdlNGJmZTgxZWQwNDNkODQ4\nNDU4YzYwMiIsImxvd1NwZWVkRHVyYXRpb24iOjAsImxvd1NwZWVkRmVlIjowLCJkaXN0YW5jZUFs\nbG93YW5jZUZlZSI6MCwidGF4aURpc3BhdGNoRmVlIjowLCJmdWVsRmVlIjowLCJkaXNwYXRjaFJp\nc2VGZWUiOjAsImhvbGlkYXlSaXNlRmVlIjoxMDAsInRheGlGZWUiOjB9LHsib3JkZXJObyI6IlQ0\naXoxNm45dzI3YzNlNzAxNGZjZDI0NDcwOTdjY2RiYTIyZGI1NDg2OCIsImJhc2VGZWUiOjY5ODA2\nLCJleHRyYUZlZSI6MCwidG90YWxGZWUiOjcwMDA1LCJmaXhlZFByaWNlIjowLCJkdXJhdGlvbiI6\nMjY3OSwiZHVyYXRpb25GZWUiOjEwMzk1LCJkaXN0YW5jZSI6NDQ2NTAsImRpc3RhbmNlRmVlIjo4\nMzMwLCJtaW5GZWUiOjEyMDAsInBhcmtGZWUiOjAsIndhaXRGZWUiOjAsImJyaWRnZUZlZSI6MCwi\nY2xlYXJGZWUiOjAsImxvbmdEaXN0YW5jZUZlZSI6NDk5ODAsImxvbmdEaXN0YW5jZSI6NDE2NTAs\nImNyb3NzQ2l0eUZlZSI6MCwiZGlzcGF0Y2hGZWUiOjAsIm5pZ2h0RmVlIjowLCJvdmVydGltZUZl\nZSI6MCwib3ZlcnRpbWUiOjAsImNhbmNlbEZlZSI6MCwiZmVlVHlwZSI6OCwidXBkYXRlVGltZSI6\nIjIwMjEtMTItMTMgMDM6MjY6NDciLCJjcmVhdGVUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNjo0NyIs\nImFkanVzdEZlZSI6MCwiY291cG9uVHlwZSI6MCwiY291cG9uQW1vdW50IjowLCJwYXJ0aXRpb25J\nbmRleCI6MCwicGxhY2FyZEZlZSI6MCwib3RoZXJGZWUiOjAsInBsYXRmb3JtTWVzc2FnZUZlZSI6\nMTk5LCJwYXNzZW5nZXJDb25maXJtIjowLCJiYXNlVGltZSI6MTAsImJhc2VNaWxlYWdlIjozMDAw\nLCJleHRyYURpc3RhbmNlIjo0MTY1MCwiZXh0cmFEdXJhdGlvbiI6MjA3OSwidmFsdWF0aW9uTW9k\nZSI6MiwibGVzc1RoYW5TdGFydEZlZSI6MCwid2FpdFRpbWUiOjAsImNvdXBvblZhbHVlIjowLCJj\naGVhcEFtb3VudCI6MCwiY2hvb3NlRHJpdmVyRmVlIjowLCJjb21taXNzaW9uRmVlIjowLCJlbnRT\nZXJ2aWNlRmVlIjowLCJ0ZW1wUmlzZUZlZSI6MCwiZmVlU3ViVHlwZSI6MSwicGlja3VwRXRhIjow\nLCJwaWNrdXBFZGEiOjAsImVzdGltYXRlSWQiOiIyMTEyMTM4YTY3MDcwZWE5N2U0YmZlODFlZDA0\nM2Q4NDg0NThjNjAyIiwibG93U3BlZWREdXJhdGlvbiI6MCwibG93U3BlZWRGZWUiOjAsImRpc3Rh\nbmNlQWxsb3dhbmNlRmVlIjowLCJ0YXhpRGlzcGF0Y2hGZWUiOjAsImZ1ZWxGZWUiOjAsImRpc3Bh\ndGNoUmlzZUZlZSI6MCwiaG9saWRheVJpc2VGZWUiOjEwMCwidGF4aUZlZSI6MH1dLCJwYXltZW50\nSW5mbyI6W3sib3JkZXJObyI6IlQ0aXoxNm45dzI3YzNlNzAxNGZjZDI0NDcwOTdjY2RiYTIyZGI1\nNDg2OCIsInRyaXBObyI6IlQ0aXoxNm45dzIxMjE2MmYzMzAxYzgxNDQ4MDlhMTBjOTcyYzliYTA5\nMDNhMSIsInJlcXVlc3RJZCI6IjIxMTIxMzhhNjcwNzBlYTk3ZTRiZmU4MWVkMDQzZDg0ODQ1OGM2\nMDIiLCJwYXlPcmRlck5vIjoic2l0MjAyMTEyMTMwMzI3MDAwNDkyMTI0MDY5MlRFU1QiLCJwYXlC\naXpUeXBlIjoyMCwic3RhdHVzIjoxLCJ1cGRhdGVUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNzowMyIs\nImNyZWF0ZVRpbWUiOiIyMDIxLTEyLTEzIDAzOjI2OjUzIiwicGF5Q2hhbm5lbCI6IjEiLCJwYXll\nciI6MSwiYWN0dWFsSW5mbyI6IntcImFwcElkXCI6IFwic2FpY19jYXJcIiwgXCJwYXlUaW1lXCI6\nIFwiMjAyMS0xMi0xMyAwMzoyNzowMlwiLCBcImNvdXBvbklkXCI6IDAsIFwicGFpZEluZm9cIjog\nXCJbe1xcXCJhY3R1YWxBZ2dzY0NoYW5uZWxUeXBlXFxcIjpcXFwiXFxcIixcXFwiY2FwaXRhbEFt\nb3VudFxcXCI6MCxcXFwiY2hhbm5lbElkXFxcIjo0LFxcXCJjaGFubmVsT3JkZXJOb1xcXCI6XFxc\nIlQwMjExMTAzODkwNzM5XFxcIixcXFwiY2hhbm5lbFNlcU5vXFxcIjpcXFwiMjAyMTExMDMyMjAw\nMTQ0Nzc5MTQxMDc5Mjc3NlxcXCIsXFxcImVudElkXFxcIjowLFxcXCJlbnRQYXlNb2RlbFxcXCI6\nMyxcXFwiZXF1aXR5QW1vdW50XFxcIjowLFxcXCJtZXJnZUZsYWdcXFwiOjAsXFxcInBhaWRcXFwi\nOjE4MDAsXFxcInBheUNoYW5uZWxOYW1lXFxcIjpcXFwi5pSv5LuY5a6d5pSv5LuYXFxcIixcXFwi\ncGF5T3JkZXJOb1xcXCI6XFxcInNpdDIwMjExMjEzMDMyNzAwMDQ5MjEyNDA2OTJURVNUXFxcIixc\nXFwicGF5U2NlbmVcXFwiOjMsXFxcInBheVNjZW5lVGV4dFxcXCI6XFxcIumihOS7mFxcXCIsXFxc\nInBheWNoYW5uZWxcXFwiOjEsXFxcInRyYW5zYWN0aW9uTm9cXFwiOlxcXCJUZGQ3YmVkOGZlNWI5\nNGRjMWJiMTFiMWJjODQ0YzE3MmVcXFwiLFxcXCJ0cmFuc2FjdGlvblRpbWVcXFwiOlxcXCIyMDIx\nLTEyLTEzIDAzOjI3OjAyXFxcIn1dXCIsIFwiY291cG9uRm9ybVwiOiAwLCBcImNvdXBvblR5cGVc\nIjogMCwgXCJlbXBsb3llZUlkXCI6IFwiXCIsIFwiZW50cHJpc2VJZFwiOiBcIlwiLCBcIm1lcmNo\nYW50SWRcIjogXCJzYWljX2NhclwiLCBcInBheUNoYW5uZWxcIjogXCIxXCIsIFwiY2hlYXBBbW91\nbnRcIjogMCwgXCJjb21wYW55TmFtZVwiOiBcIlwiLCBcImNvdXBvblRpdGxlXCI6IFwiXCIsIFwi\nY291cG9uVmFsdWVcIjogMCwgXCJhY3R1YWxBbW91bnRcIjogMTgwMCwgXCJjb3Vwb25BbW91bnRc\nIjogMCwgXCJkcml2ZXJBbW91bnRcIjogMTI1MCwgXCJiYWxhbmNlQW1vdW50XCI6IDAsIFwicmV2\nZW51ZUFtb3VudFwiOiA1NTAsIFwicGF5Q2hhbm5lbE5hbWVcIjogXCLmlK/ku5jlrp3mlK/ku5hc\nIiwgXCJ0aGlyZFBhcnR5Q291cG9uQW1vdW50XCI6IDB9IiwicHJpY2VJbmZvIjoiXCJ7fVwiIn1d\nLCJ0YWdNSW5mbyI6eyJhaXJwbGFuZSI6MSwidXNlRWFzIjowLCJyZXBsYWNlIjowLCJmb3JlaWdu\nIjoyLCJrdW5zaGFuIjowLCJwYXlBZHZhbmNlIjowLCJyZWZ1bmQiOjAsImJlY2tvbiI6MCwicmVs\nYXkiOjAsImJ5V2F5IjowLCJyZWRpc3BhdGNoIjowLCJjcm9zc0NpdHkiOjAsImV4Y2VwdGlvbiI6\nMSwiYWxhcm1QIjowLCJhbGFybUQiOjAsInNoYXJlIjowLCJtb2RpZnlQcmljZSI6MCwicGF5QnlQ\nbGF0Zm9ybSI6MCwiZXhwaXJhdGlvblRpbWUiOiIyMDAwLTAxLTAxIDAxOjAxOjAxIn0sInRyYW5z\nSW5uZXJNSW5mbyI6eyJkaXNwYXRjaFRpbWUiOiIyMDIxLTEyLTEzIDAzOjI2OjQ4Iiwic2Vydmlj\nZVN0YXJ0VGltZSI6IjIwMjEtMTItMTMgMDM6MjY6NTIiLCJhcnJpdmVCb2FyZGluZ1RpbWUiOiIy\nMDIxLTEyLTEzIDAzOjI2OjUyIiwicGlja1VwVGltZSI6IjIwMjEtMTItMTMgMDM6MjY6NTIiLCJh\ncnJpdmVUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNjo1MyIsInBheVRpbWUiOiIyMDIxLTEyLTEzIDAz\nOjI3OjAzIn0sInRyYW5zT3V0ZXJJbmZvIjpbeyJvcmRlck5vIjoiVDRpejE2bjl3MjdjM2U3MDE0\nZmNkMjQ0NzA5N2NjZGJhMjJkYjU0ODY4IiwiZXZlbnRDb2RlIjoiNjAxMCIsImV2ZW50RGV0YWls\nIjoie1wiaXNDYW5jZWxcIjowfSIsInVzZXJJZCI6IlAyZWEyYjg3ZGYwZTU0MGM5OTBhMGY3ZjAw\nYWNiZTE2OCIsInVzZXJUeXBlIjoxLCJjcmVhdGVUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNjo0NyJ9\nLHsib3JkZXJObyI6IlQ0aXoxNm45dzI3YzNlNzAxNGZjZDI0NDcwOTdjY2RiYTIyZGI1NDg2OCIs\nImV2ZW50Q29kZSI6IjYwMTAiLCJldmVudERldGFpbCI6IntcImlzQ2FuY2VsXCI6MH0iLCJ1c2Vy\nSWQiOiJEYzVlMjBkMjBhNWRlNDE4NWJkZDRiMGM1MTM0MTY5MTIiLCJ1c2VyVHlwZSI6MiwiY3Jl\nYXRlVGltZSI6IjIwMjEtMTItMTMgMDM6MjY6NDcifV0sInRyYW5zSW5uZXJJbmZvIjpbeyJvcmRl\nck5vIjoiVDRpejE2bjl3MjdjM2U3MDE0ZmNkMjQ0NzA5N2NjZGJhMjJkYjU0ODY4IiwiZXZlbnRD\nb2RlIjoiYXJyaXZlQW5kU2V0dGxlbWVudCIsImV2ZW50RGV0YWlsIjoie1wibmFtZVwiOiBcIuWI\nsOi+vuW5tue7k+eul1wifSIsInVzZXJUeXBlIjowLCJ0cmFuc1RpbWUiOiIyMDIxLTEyLTEzIDAz\nOjI2OjUzIiwidXBkYXRlVGltZSI6IjIwMjEtMTItMTMgMDM6MjY6NTMiLCJjcmVhdGVUaW1lIjoi\nMjAyMS0xMi0xMyAwMzoyNjo1MyIsImZyb21TdGF0ZSI6MCwidG9TdGF0ZSI6MCwib3BlcmF0b3JU\neXBlIjoxLCJvcGVyYXRvciI6MCwiZHJpdmVyTG9jYXRpb24iOiIxMjEuNDc1MTY0LDMxLjIyODgx\nNiIsImRyaXZlclBvaUFkZHJlc3MiOiLkuIrmtbfkurrmsJHlub/lnLrkuIrmtbfljZrnianppoYi\nLCJkcml2ZXJEZXRhaWxBZGRyZXNzIjoi5LiK5rW35biC6buE5rWm5Yy65Lq65rCR5aSn6YGTMTIw\n5Y+3IiwicGFydGl0aW9uSW5kZXgiOjB9LHsib3JkZXJObyI6IlQ0aXoxNm45dzI3YzNlNzAxNGZj\nZDI0NDcwOTdjY2RiYTIyZGI1NDg2OCIsImV2ZW50Q29kZSI6ImFycml2ZUJvYXJkaW5nIiwiZXZl\nbnREZXRhaWwiOiJ7XCJhcnJpdmVCb2FyZGluZ0VkYVwiOiA0MTU0OSwgXCJhcnJpdmVCb2FyZGlu\nZ0V0YVwiOiAyMzE1fSIsInVzZXJUeXBlIjowLCJ0cmFuc1RpbWUiOiIyMDIxLTEyLTEzIDAzOjI2\nOjUyIiwidXBkYXRlVGltZSI6IjIwMjEtMTItMTMgMDM6MjY6NTIiLCJjcmVhdGVUaW1lIjoiMjAy\nMS0xMi0xMyAwMzoyNjo1MiIsImZyb21TdGF0ZSI6MCwidG9TdGF0ZSI6MCwib3BlcmF0b3JUeXBl\nIjoxLCJvcGVyYXRvciI6MCwiZHJpdmVyTG9jYXRpb24iOiIxMjEuNDc2NjEyLDMxLjIxMTI2NiIs\nImRyaXZlclBvaUFkZHJlc3MiOiLoibrov6rluIzoiJ7ouYjloZHlvaLkuK3lv4Mo5paw5aSp5Zyw\n5bqXKeS4rea1t+eOr+Wuh+iNnyIsImRyaXZlckRldGFpbEFkZHJlc3MiOiLkuIrmtbfluILpu4Tm\ntabljLrpqazlvZPot68zMeWPtyIsInBhcnRpdGlvbkluZGV4IjowfSx7Im9yZGVyTm8iOiJUNGl6\nMTZuOXcyN2MzZTcwMTRmY2QyNDQ3MDk3Y2NkYmEyMmRiNTQ4NjgiLCJldmVudENvZGUiOiJqdWRn\nZVF1aWNrVHJpcENvbXBsZXRlT3JkZXIiLCJldmVudERldGFpbCI6IntcIm5hbWVcIjogXCLlrozl\njZXliKTmlq3lv6vpgJ/ooYznqItcIiwgXCJqb2JTb3VyY2VcIjogXCJkb0Fycml2ZUFuZFNldHRs\nZW1lbnRcIn0iLCJ1c2VyVHlwZSI6MCwidHJhbnNUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNzo1NCIs\nInVwZGF0ZVRpbWUiOiIyMDIxLTEyLTEzIDAzOjI3OjU0IiwiY3JlYXRlVGltZSI6IjIwMjEtMTIt\nMTMgMDM6Mjc6NTQiLCJmcm9tU3RhdGUiOjAsInRvU3RhdGUiOjAsIm9wZXJhdG9yVHlwZSI6MzAs\nIm9wZXJhdG9yIjowLCJwYXJ0aXRpb25JbmRleCI6MH0seyJvcmRlck5vIjoiVDRpejE2bjl3Mjdj\nM2U3MDE0ZmNkMjQ0NzA5N2NjZGJhMjJkYjU0ODY4IiwiZXZlbnRDb2RlIjoibWF0Y2hTdWNjZWVk\nIiwiZXZlbnREZXRhaWwiOiJ7XCJuYW1lXCI6IFwi5rS+5Y2V5oiQ5YqfXCIsIFwiZXRhQnVmZmVy\nXCI6IDAsIFwiZHJpdmVyRXh0TGF0XCI6IFwiMC4wXCIsIFwiZHJpdmVyRXh0TG9uXCI6IFwiMC4w\nXCJ9IiwidXNlclR5cGUiOjAsInRyYW5zVGltZSI6IjIwMjEtMTItMTMgMDM6MjY6NDgiLCJ1cGRh\ndGVUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNjo0NyIsImNyZWF0ZVRpbWUiOiIyMDIxLTEyLTEzIDAz\nOjI2OjQ3IiwiZnJvbVN0YXRlIjowLCJ0b1N0YXRlIjowLCJvcGVyYXRvclR5cGUiOjMwLCJvcGVy\nYXRvciI6MCwicGFzc2VuZ2VyTG9jYXRpb24iOiIxMjEuODAyOTk5LDMxLjE0OTQ4NyIsImRyaXZl\nckxvY2F0aW9uIjoiMTIxLjQ3NjYxMiwzMS4yMTEyNjYiLCJwYXNzZW5nZXJQb2lBZGRyZXNzIjoi\n5LiK5rW35rWm5Lic5Zu96ZmF5py65Zy6MeWPt+iIquermealvCIsInBhc3NlbmdlckRldGFpbEFk\nZHJlc3MiOiLmnLrlnLrplYfnuqzkuIDot68xMDDlj7ciLCJkcml2ZXJQb2lBZGRyZXNzIjoi6Im6\n6L+q5biM6Iie6LmI5aGR5b2i5Lit5b+DKOaWsOWkqeWcsOW6lynkuK3mtbfnjq/lrofojZ8iLCJk\ncml2ZXJEZXRhaWxBZGRyZXNzIjoi5LiK5rW35biC6buE5rWm5Yy66ams5b2T6LevMzHlj7ciLCJw\nYXJ0aXRpb25JbmRleCI6MH0seyJvcmRlck5vIjoiVDRpejE2bjl3MjdjM2U3MDE0ZmNkMjQ0NzA5\nN2NjZGJhMjJkYjU0ODY4IiwiZXZlbnRDb2RlIjoicGF5bm90aWZ5IiwidXNlclR5cGUiOjAsInRy\nYW5zVGltZSI6IjIwMjEtMTItMTMgMDM6Mjc6MDMiLCJ1cGRhdGVUaW1lIjoiMjAyMS0xMi0xMyAw\nMzoyNzowMyIsImNyZWF0ZVRpbWUiOiIyMDIxLTEyLTEzIDAzOjI3OjAzIiwiZnJvbVN0YXRlIjow\nLCJ0b1N0YXRlIjowLCJvcGVyYXRvclR5cGUiOjAsIm9wZXJhdG9yIjowLCJwYXJ0aXRpb25JbmRl\neCI6MH0seyJvcmRlck5vIjoiVDRpejE2bjl3MjdjM2U3MDE0ZmNkMjQ0NzA5N2NjZGJhMjJkYjU0\nODY4IiwiZXZlbnRDb2RlIjoicGlja3VwUGFzc2VuZ2VyIiwiZXZlbnREZXRhaWwiOiJ7XCJuYW1l\nXCI6IFwi5o6l5Yiw5LmY5a6iXCJ9IiwidXNlclR5cGUiOjAsInRyYW5zVGltZSI6IjIwMjEtMTIt\nMTMgMDM6MjY6NTIiLCJ1cGRhdGVUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNjo1MiIsImNyZWF0ZVRp\nbWUiOiIyMDIxLTEyLTEzIDAzOjI2OjUyIiwiZnJvbVN0YXRlIjowLCJ0b1N0YXRlIjowLCJvcGVy\nYXRvclR5cGUiOjAsIm9wZXJhdG9yIjowLCJkcml2ZXJMb2NhdGlvbiI6IjEyMS40NzY2MTIsMzEu\nMjExMjY2IiwiZHJpdmVyUG9pQWRkcmVzcyI6IuelneahpemVh+S4iua1t+a1puS4nOWbvemZheac\nuuWcujHlj7foiKrnq5nmpbwiLCJkcml2ZXJEZXRhaWxBZGRyZXNzIjoi5LiK5rW35biC5rWm5Lic\n5paw5Yy65ZCv6Iiq6LevOTAw5Y+3IiwicGFydGl0aW9uSW5kZXgiOjB9LHsib3JkZXJObyI6IlQ0\naXoxNm45dzI3YzNlNzAxNGZjZDI0NDcwOTdjY2RiYTIyZGI1NDg2OCIsImV2ZW50Q29kZSI6InN0\nYXJ0U2VydmljZSIsImV2ZW50RGV0YWlsIjoie1wibmFtZVwiOiBcIumihOe6puWNleWPuOacuuW8\ngOWni+acjeWKoVwifSIsInVzZXJUeXBlIjowLCJ0cmFuc1RpbWUiOiIyMDIxLTEyLTEzIDAzOjI2\nOjUyIiwidXBkYXRlVGltZSI6IjIwMjEtMTItMTMgMDM6MjY6NTIiLCJjcmVhdGVUaW1lIjoiMjAy\nMS0xMi0xMyAwMzoyNjo1MiIsImZyb21TdGF0ZSI6MCwidG9TdGF0ZSI6MCwib3BlcmF0b3JUeXBl\nIjowLCJvcGVyYXRvciI6MCwiZHJpdmVyTG9jYXRpb24iOiIxMjEuNDc2NjEyLDMxLjIxMTI2NiIs\nInBhcnRpdGlvbkluZGV4IjowfV0sImd1ZXN0SW5mbyI6W3siZ3Vlc3ROYW1lIjoiMTEzKioqKjA4\nMzciLCJndWVzdE1vYmlsZSI6IjExMzMxMDEwODM3IiwiaXNTZW5kTXNnIjowLCJpc1NlbmRFbWFp\nbCI6MCwiaXNEZWZhdWx0IjoxfV0sInJlZnVuZEFtb3VudCI6MCwidGFnSW5mbyI6W3sib3JkZXJO\nbyI6IlQ0aXoxNm45dzI3YzNlNzAxNGZjZDI0NDcwOTdjY2RiYTIyZGI1NDg2OCIsInRhZ1R5cGUi\nOjEsInRhZ1ZhbHVlIjoiVEcwMTAwMSIsInJlbWFyayI6IuWPuOacuuWIsOi+vuS4iui9pueCuei2\nhei/h+iMg+WbtOW8guW4uCzopoHmsYLojIPlm7Q6MTAx57GzIOWunumZheiMg+WbtDozMTgwMSDn\nsbMiLCJjcmVhdGVUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNjo1MiIsInVwZGF0ZVRpbWUiOiIyMDIx\nLTEyLTEzIDAzOjI2OjUyIn0seyJvcmRlck5vIjoiVDRpejE2bjl3MjdjM2U3MDE0ZmNkMjQ0NzA5\nN2NjZGJhMjJkYjU0ODY4IiwidGFnVHlwZSI6OCwidGFnVmFsdWUiOiJURzA2MDAyIiwicmVtYXJr\nIjoi5Y+45py65bey6K+EIiwiY3JlYXRlVGltZSI6IjIwMjEtMTItMTMgMDM6MjY6NTUiLCJ1cGRh\ndGVUaW1lIjoiMjAyMS0xMi0xMyAwMzoyNjo1NSJ9LHsib3JkZXJObyI6IlQ0aXoxNm45dzI3YzNl\nNzAxNGZjZDI0NDcwOTdjY2RiYTIyZGI1NDg2OCIsInRhZ1R5cGUiOjE5LCJ0YWdWYWx1ZSI6IlRH\nMDEzMDAwIiwicmVtYXJrIjoi6aOO5o6nLeWujOWNleato+W4uCIsImNyZWF0ZVRpbWUiOiIyMDIx\nLTEyLTEzIDAzOjI3OjU0IiwidXBkYXRlVGltZSI6IjIwMjEtMTItMTMgMDM6Mjc6NTQifV0sImRp\nc3BhdGNoQWdhaW5UYXNrSW5mbyI6eyJvcGVyYXRvclR5cGUiOjAsIm5lZWRDb3VudCI6MCwic3Rh\ndHVzIjowLCJyZXdhcmRBbW91bnQiOjAsInB1bmlzaEFtb3VudCI6MCwicmlnaHRGbGFnIjowLCJy\naWdodFNjb3JlIjowLCJkaXNwYXRjaE1vZGUiOjB9LCJwcm9wZXJ0eUluZm8iOlt7Im9yZGVyTm8i\nOiJUNGl6MTZuOXcyN2MzZTcwMTRmY2QyNDQ3MDk3Y2NkYmEyMmRiNTQ4NjgiLCJ0cmlwTm8iOiJU\nNGl6MTZuOXcyMTIxNjJmMzMwMWM4MTQ0ODA5YTEwYzk3MmM5YmEwOTAzYTEiLCJwcm9wZXJ0eUlk\nIjoiRlVDIiwidXNlclByb3BlcnR5SWQiOiJGVUMiLCJ1c2VWYWx1ZSI6MCwic3RhdHVzIjo0LCJw\ncm9wZXJ0eVR5cGUiOjB9XSwiZHJpdmluZ1NpdHVhdGlvbkluZm8iOnsidGVtcGVyYXR1cmUiOjAs\nImRpc3RhbmNlIjowLCJkdXJhdGlvbiI6MCwiYXZnU3BlZWQiOjAsImF1dG9SYXRlIjowLCJ0cmFm\nZmljTW90b3JRdHkiOjAsInRyYWZmaWNOb25Nb3RvclF0eSI6MCwidHJhZmZpY1BlZGVzdHJpYW5R\ndHkiOjAsImFpTGV2ZWwiOjAsImFpTGV2ZWxQcm9ncmVzcyI6MH19",
                "clientIp": "",
                "reqBody":
                "{productId=1, orderNo=T4iz16n9w27c3e7014fcd2447097ccdba22db54868}",
                "resHeader": ""
            },
            "type": 36,
            "version": "v2"
        }
        data['detail']['agentId'] = self.agent_id
        res = self.agent_report(data, agentId=self.agent_id)

