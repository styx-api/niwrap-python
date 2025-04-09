# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF_DSET_INFO_METADATA = Metadata(
    id="9666989bfdfef6c61d4a14a8494e8f393de0b2fa.boutiques",
    name="SurfDsetInfo",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


SurfDsetInfoParameters = typing.TypedDict('SurfDsetInfoParameters', {
    "__STYX_TYPE__": typing.Literal["SurfDsetInfo"],
    "input_dsets": list[InputPathType],
    "debug_level": typing.NotRequired[int | None],
    "novolreg": bool,
    "noxform": bool,
    "setenv": typing.NotRequired[str | None],
    "trace": bool,
    "extreme_trace": bool,
    "nomall": bool,
    "yesmall": bool,
    "mini_help": bool,
    "help": bool,
    "extreme_help": bool,
    "help_view": bool,
    "help_web": bool,
    "help_find": typing.NotRequired[str | None],
    "help_raw": bool,
    "help_spx": bool,
    "help_aspx": bool,
    "all_opts": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "SurfDsetInfo": surf_dset_info_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class SurfDsetInfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_dset_info(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surf_dset_info_params(
    input_dsets: list[InputPathType],
    debug_level: int | None = None,
    novolreg: bool = False,
    noxform: bool = False,
    setenv: str | None = None,
    trace_: bool = False,
    extreme_trace: bool = False,
    nomall: bool = False,
    yesmall: bool = False,
    mini_help: bool = False,
    help_: bool = False,
    extreme_help: bool = False,
    help_view: bool = False,
    help_web: bool = False,
    help_find: str | None = None,
    help_raw: bool = False,
    help_spx: bool = False,
    help_aspx: bool = False,
    all_opts: bool = False,
) -> SurfDsetInfoParameters:
    """
    Build parameters.
    
    Args:
        input_dsets: Input dataset.
        debug_level: Debug level. If DBG = 2, show full dataset information in\
            NIML form.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations.
        noxform: Same as -novolreg.
        setenv: Set environment variable.
        trace_: Turns on In/Out debug and Memory tracing.
        extreme_trace: Turns on extreme tracing.
        nomall: Turn off memory tracing.
        yesmall: Turn on memory tracing (default).
        mini_help: Mini help.
        help_: Show entire help output.
        extreme_help: Show extreme help.
        help_view: Open help in text editor.
        help_web: Open help in web browser.
        help_find: Look for lines in help output that match the specified word.
        help_raw: Show unedited help string.
        help_spx: Show help string in sphinx format, but do not autoformat.
        help_aspx: Show help string in sphinx with autoformatting.
        all_opts: Attempt to identify all options for the program from the help\
            output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfDsetInfo",
        "input_dsets": input_dsets,
        "novolreg": novolreg,
        "noxform": noxform,
        "trace": trace_,
        "extreme_trace": extreme_trace,
        "nomall": nomall,
        "yesmall": yesmall,
        "mini_help": mini_help,
        "help": help_,
        "extreme_help": extreme_help,
        "help_view": help_view,
        "help_web": help_web,
        "help_raw": help_raw,
        "help_spx": help_spx,
        "help_aspx": help_aspx,
        "all_opts": all_opts,
    }
    if debug_level is not None:
        params["debug_level"] = debug_level
    if setenv is not None:
        params["setenv"] = setenv
    if help_find is not None:
        params["help_find"] = help_find
    return params


def surf_dset_info_cargs(
    params: SurfDsetInfoParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("SurfDsetInfo")
    cargs.extend([
        "-input",
        *[execution.input_file(f) for f in params.get("input_dsets")]
    ])
    if params.get("debug_level") is not None:
        cargs.extend([
            "-debug",
            str(params.get("debug_level"))
        ])
    if params.get("novolreg"):
        cargs.append("-novolreg")
    if params.get("noxform"):
        cargs.append("-noxform")
    if params.get("setenv") is not None:
        cargs.extend([
            "-setenv",
            params.get("setenv")
        ])
    if params.get("trace"):
        cargs.append("-trace")
    if params.get("extreme_trace"):
        cargs.append("-TRACE")
    if params.get("nomall"):
        cargs.append("-nomall")
    if params.get("yesmall"):
        cargs.append("-yesmall")
    if params.get("mini_help"):
        cargs.append("-h")
    if params.get("help"):
        cargs.append("-help")
    if params.get("extreme_help"):
        cargs.append("-HELP")
    if params.get("help_view"):
        cargs.append("-h_view")
    if params.get("help_web"):
        cargs.append("-h_web")
    if params.get("help_find") is not None:
        cargs.extend([
            "-h_find",
            params.get("help_find")
        ])
    if params.get("help_raw"):
        cargs.append("-h_raw")
    if params.get("help_spx"):
        cargs.append("-h_spx")
    if params.get("help_aspx"):
        cargs.append("-h_aspx")
    if params.get("all_opts"):
        cargs.append("-all_opts")
    return cargs


def surf_dset_info_outputs(
    params: SurfDsetInfoParameters,
    execution: Execution,
) -> SurfDsetInfoOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfDsetInfoOutputs(
        root=execution.output_file("."),
    )
    return ret


def surf_dset_info_execute(
    params: SurfDsetInfoParameters,
    execution: Execution,
) -> SurfDsetInfoOutputs:
    """
    Provides information about surface datasets (DSET).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfDsetInfoOutputs`).
    """
    params = execution.params(params)
    cargs = surf_dset_info_cargs(params, execution)
    ret = surf_dset_info_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_dset_info(
    input_dsets: list[InputPathType],
    debug_level: int | None = None,
    novolreg: bool = False,
    noxform: bool = False,
    setenv: str | None = None,
    trace_: bool = False,
    extreme_trace: bool = False,
    nomall: bool = False,
    yesmall: bool = False,
    mini_help: bool = False,
    help_: bool = False,
    extreme_help: bool = False,
    help_view: bool = False,
    help_web: bool = False,
    help_find: str | None = None,
    help_raw: bool = False,
    help_spx: bool = False,
    help_aspx: bool = False,
    all_opts: bool = False,
    runner: Runner | None = None,
) -> SurfDsetInfoOutputs:
    """
    Provides information about surface datasets (DSET).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dsets: Input dataset.
        debug_level: Debug level. If DBG = 2, show full dataset information in\
            NIML form.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations.
        noxform: Same as -novolreg.
        setenv: Set environment variable.
        trace_: Turns on In/Out debug and Memory tracing.
        extreme_trace: Turns on extreme tracing.
        nomall: Turn off memory tracing.
        yesmall: Turn on memory tracing (default).
        mini_help: Mini help.
        help_: Show entire help output.
        extreme_help: Show extreme help.
        help_view: Open help in text editor.
        help_web: Open help in web browser.
        help_find: Look for lines in help output that match the specified word.
        help_raw: Show unedited help string.
        help_spx: Show help string in sphinx format, but do not autoformat.
        help_aspx: Show help string in sphinx with autoformatting.
        all_opts: Attempt to identify all options for the program from the help\
            output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfDsetInfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_DSET_INFO_METADATA)
    params = surf_dset_info_params(
        input_dsets=input_dsets,
        debug_level=debug_level,
        novolreg=novolreg,
        noxform=noxform,
        setenv=setenv,
        trace_=trace_,
        extreme_trace=extreme_trace,
        nomall=nomall,
        yesmall=yesmall,
        mini_help=mini_help,
        help_=help_,
        extreme_help=extreme_help,
        help_view=help_view,
        help_web=help_web,
        help_find=help_find,
        help_raw=help_raw,
        help_spx=help_spx,
        help_aspx=help_aspx,
        all_opts=all_opts,
    )
    return surf_dset_info_execute(params, execution)


__all__ = [
    "SURF_DSET_INFO_METADATA",
    "SurfDsetInfoOutputs",
    "SurfDsetInfoParameters",
    "surf_dset_info",
    "surf_dset_info_params",
]
