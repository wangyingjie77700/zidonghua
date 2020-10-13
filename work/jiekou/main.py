import unittest
import jsonpath
from ddt import ddt, data, unpack
from jiekou.exceloperator import excelData
from jiekou.operator_Common import operator_Common
from jiekou.convertoperator import convertConvert,depend

@ddt
class MyTestCase(unittest.TestCase):

    @data(*excelData().getExcel())
    @unpack
    def test_get(self, url, body, header, method, method_type,exceptvalue,jsonpathvalue,dependency):
        comon=operator_Common()
        body = "" if body is None else body
        header = "" if header is None else header
        body=convertConvert().convertOp(body) if body.find("$") >=0 else body
        header=convertConvert().convertOp(header) if header.find("$")>=0 else header

        res=comon.request(method,url,method_type,body,header)


        if len(dependency) >0 and dependency.find("/") < 0:
            depend[dependency]=res.content

        print(res.json())
        code=res.status_code
        jsonpathexcept=jsonpath.jsonpath(res.json(),jsonpathvalue)

        self.assertEqual(exceptvalue, jsonpathexcept[0])



