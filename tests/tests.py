# Copyright 2019 Vitaliy Zakaznikov, TestFlows Test Framework (http://testflows.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from testflows.core import main, test
from testflows.core import Test as TestBase

class Test(TestBase):
    def run(self):
        prompt = r'[#\$] '

        with test("import uexpect"):
            from testflows.uexpect import spawn

        with test("spawn bash terminal") as test:
            terminal1 = spawn(["/bin/bash", "--noediting"])
            terminal2 = spawn(["/bin/bash", "--noediting"])
           
            terminal1.eol("\r")
            terminal1.timeout(10)
            terminal1.logger(test.message_io("terminal1"))

            terminal2.eol("\r")
            terminal2.timeout(10)
            terminal2.logger(test.message_io("terminal2"))

            terminal1.expect(prompt)
            terminal2.expect(prompt)

            terminal2.send("echo foo")
            terminal2.expect(prompt)
            terminal1.send("echo $?")
            terminal1.expect(prompt)

        with test("print() using test.message_io()"):
            print("hello there", file=test.message_io("print"))
            print("another", file=test.message_io("print"))

if main():
    with Test("regression"):
        pass
