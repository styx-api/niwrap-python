# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SERIAL_HELPER_METADATA = Metadata(
    id="4df7ea7f38a6767c1aba72a89599b9e5c022108c.boutiques",
    name="serial_helper",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


SerialHelperParameters = typing.TypedDict('SerialHelperParameters', {
    "__STYX_TYPE__": typing.Literal["serial_helper"],
    "serial_port": str,
    "sock_num": typing.NotRequired[float | None],
    "mp_max": typing.NotRequired[float | None],
    "mp_min": typing.NotRequired[float | None],
    "num_extra": typing.NotRequired[float | None],
    "disp_all": typing.NotRequired[float | None],
    "debug": typing.NotRequired[float | None],
    "show_times": bool,
    "help": bool,
    "hist": bool,
    "no_serial": bool,
    "version": bool,
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
        "serial_helper": serial_helper_cargs,
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


class SerialHelperOutputs(typing.NamedTuple):
    """
    Output object returned when calling `serial_helper(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def serial_helper_params(
    serial_port: str,
    sock_num: float | None = None,
    mp_max: float | None = None,
    mp_min: float | None = None,
    num_extra: float | None = None,
    disp_all: float | None = None,
    debug: float | None = None,
    show_times: bool = False,
    help_: bool = False,
    hist: bool = False,
    no_serial: bool = False,
    version: bool = False,
) -> SerialHelperParameters:
    """
    Build parameters.
    
    Args:
        serial_port: Output serial port filename.
        sock_num: Specify socket number to serve.
        mp_max: Limit the maximum value of the MP data.
        mp_min: Limit the minimum value of the MP data.
        num_extra: Receive additional floats per TR.
        disp_all: Receive NVOX*8 extra floats per TR.
        debug: Set the debugging level (0-3).
        show_times: Show communication times.
        help_: Display this help information.
        hist: Show the module history.
        no_serial: Turn off serial port output.
        version: Show the current version number.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "serial_helper",
        "serial_port": serial_port,
        "show_times": show_times,
        "help": help_,
        "hist": hist,
        "no_serial": no_serial,
        "version": version,
    }
    if sock_num is not None:
        params["sock_num"] = sock_num
    if mp_max is not None:
        params["mp_max"] = mp_max
    if mp_min is not None:
        params["mp_min"] = mp_min
    if num_extra is not None:
        params["num_extra"] = num_extra
    if disp_all is not None:
        params["disp_all"] = disp_all
    if debug is not None:
        params["debug"] = debug
    return params


def serial_helper_cargs(
    params: SerialHelperParameters,
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
    cargs.append("serial_helper")
    cargs.extend([
        "-serial_port",
        params.get("serial_port")
    ])
    if params.get("sock_num") is not None:
        cargs.extend([
            "-sock_num",
            str(params.get("sock_num"))
        ])
    if params.get("mp_max") is not None:
        cargs.extend([
            "-mp_max",
            str(params.get("mp_max"))
        ])
    if params.get("mp_min") is not None:
        cargs.extend([
            "-mp_min",
            str(params.get("mp_min"))
        ])
    if params.get("num_extra") is not None:
        cargs.extend([
            "-num_extra",
            str(params.get("num_extra"))
        ])
    if params.get("disp_all") is not None:
        cargs.extend([
            "-disp_all",
            str(params.get("disp_all"))
        ])
    if params.get("debug") is not None:
        cargs.extend([
            "-debug",
            str(params.get("debug"))
        ])
    if params.get("show_times"):
        cargs.append("-show_times")
    if params.get("help"):
        cargs.append("-help")
    if params.get("hist"):
        cargs.append("-hist")
    if params.get("no_serial"):
        cargs.append("-no_serial")
    if params.get("version"):
        cargs.append("-version")
    return cargs


def serial_helper_outputs(
    params: SerialHelperParameters,
    execution: Execution,
) -> SerialHelperOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SerialHelperOutputs(
        root=execution.output_file("."),
    )
    return ret


def serial_helper_execute(
    params: SerialHelperParameters,
    execution: Execution,
) -> SerialHelperOutputs:
    """
    Passes motion parameters from socket to serial port.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SerialHelperOutputs`).
    """
    params = execution.params(params)
    cargs = serial_helper_cargs(params, execution)
    ret = serial_helper_outputs(params, execution)
    execution.run(cargs)
    return ret


def serial_helper(
    serial_port: str,
    sock_num: float | None = None,
    mp_max: float | None = None,
    mp_min: float | None = None,
    num_extra: float | None = None,
    disp_all: float | None = None,
    debug: float | None = None,
    show_times: bool = False,
    help_: bool = False,
    hist: bool = False,
    no_serial: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> SerialHelperOutputs:
    """
    Passes motion parameters from socket to serial port.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        serial_port: Output serial port filename.
        sock_num: Specify socket number to serve.
        mp_max: Limit the maximum value of the MP data.
        mp_min: Limit the minimum value of the MP data.
        num_extra: Receive additional floats per TR.
        disp_all: Receive NVOX*8 extra floats per TR.
        debug: Set the debugging level (0-3).
        show_times: Show communication times.
        help_: Display this help information.
        hist: Show the module history.
        no_serial: Turn off serial port output.
        version: Show the current version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SerialHelperOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SERIAL_HELPER_METADATA)
    params = serial_helper_params(
        serial_port=serial_port,
        sock_num=sock_num,
        mp_max=mp_max,
        mp_min=mp_min,
        num_extra=num_extra,
        disp_all=disp_all,
        debug=debug,
        show_times=show_times,
        help_=help_,
        hist=hist,
        no_serial=no_serial,
        version=version,
    )
    return serial_helper_execute(params, execution)


__all__ = [
    "SERIAL_HELPER_METADATA",
    "SerialHelperOutputs",
    "SerialHelperParameters",
    "serial_helper",
    "serial_helper_params",
]
