cwlVersion: v1.2
class: CommandLineTool
baseCommand: echo
requirements:
 InlineJavascriptRequirement: {}
inputs:
 message:
  type: string
  default: Hello World
  inputBinding:
   position: 1
 message2:
  type: File?
  format: edam:format_2330 # textual format
  inputBinding:
   position: 2
 my_output:
  type: string
  default: outputfile
outputs:
 my_output:
  type: File
  format: edam:format_2330 # textual format
  outputBinding:
   glob: $(inputs.my_output)
stdout: $(inputs.my_output)