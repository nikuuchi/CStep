import lldb
import os


def toStringFromVariable(value):
    if value.GetValue() != None:
        return "{0}: {1} = {2}".format(value.GetTypeName(), value.GetName(), value.GetValue())
    else:
        s = "{0}: {1} = ("
        for i in range(value.num_children):
            child = value.GetChildAtIndex(i)
            s += " " + toStringFromVariable(child) + " "
        s += ")"
        return s.format(value.GetTypeName(), value.GetName())
        #print "{0}: {1} = {2}".format(value.GetTypeName(), value.GetName(), value.

exe = "./a.out"

debugger = lldb.SBDebugger.Create()
debugger.SetAsync (False)

print "Target:{0}".format(exe)

target = debugger.CreateTargetWithFileAndArch(exe, lldb.LLDB_ARCH_DEFAULT)

if target:
    main_break_point = target.BreakpointCreateByName ("main", target.GetExecutable().GetFilename())
    print main_break_point

    process = target.LaunchSimple(None, None, os.getcwd())

    state = process.GetState()
    print process
    print state

    if state == lldb.eStateStopped:
        thread = process.GetThreadAtIndex(0)
        if thread:
            while thread.stop_reason != lldb.eStateUnloaded:
                print '-' * 20
                if thread.GetNumFrames() < 2:
                    break
                for frameIndex in range(thread.GetNumFrames()):
                    frame = thread.GetFrameAtIndex(frameIndex)
                    if frame:
                        print "frame: {0}, function: {1}, line: {2}".format(frame.GetFrameID(), frame.GetFunctionName(), frame.GetLineEntry().GetLine())
                        for x in frame.GetVariables(True, True, True, True):
                            print toStringFromVariable(x)
                        print ""
                thread.StepInto()
