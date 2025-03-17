# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MYGET_METADATA = Metadata(
    id="10043a869267d2f44f577e75349933f7e7bb0e5e.boutiques",
    name="myget",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


MygetParameters = typing.TypedDict('MygetParameters', {
    "__STYX_TYPE__": typing.Literal["myget"],
    "protocol_version": typing.NotRequired[typing.Literal["-1", "-1.1"] | None],
    "url": str,
    "output_file": str,
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
        "myget": myget_cargs,
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
        "myget": myget_outputs,
    }.get(t)


class MygetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `myget(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The filename to save the downloaded file"""


def myget_params(
    url: str,
    output_file: str,
    protocol_version: typing.Literal["-1", "-1.1"] | None = None,
) -> MygetParameters:
    """
    Build parameters.
    
    Args:
        url: The URL to download the file from.
        output_file: The filename to save the downloaded file.
        protocol_version: Specify protocol version. You can choose between -1\
            or -1.1.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "myget",
        "url": url,
        "output_file": output_file,
    }
    if protocol_version is not None:
        params["protocol_version"] = protocol_version
    return params


def myget_cargs(
    params: MygetParameters,
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
    cargs.append("myget")
    if params.get("protocol_version") is not None:
        cargs.append(params.get("protocol_version"))
    cargs.append(params.get("url"))
    cargs.extend([
        ">",
        params.get("output_file")
    ])
    return cargs


def myget_outputs(
    params: MygetParameters,
    execution: Execution,
) -> MygetOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MygetOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_file")),
    )
    return ret


def myget_execute(
    params: MygetParameters,
    execution: Execution,
) -> MygetOutputs:
    """
    A simple file downloader from a URL.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MygetOutputs`).
    """
    params = execution.params(params)
    cargs = myget_cargs(params, execution)
    ret = myget_outputs(params, execution)
    execution.run(cargs)
    return ret


def myget(
    url: str,
    output_file: str,
    protocol_version: typing.Literal["-1", "-1.1"] | None = None,
    runner: Runner | None = None,
) -> MygetOutputs:
    """
    A simple file downloader from a URL.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        url: The URL to download the file from.
        output_file: The filename to save the downloaded file.
        protocol_version: Specify protocol version. You can choose between -1\
            or -1.1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MygetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MYGET_METADATA)
    params = myget_params(
        protocol_version=protocol_version,
        url=url,
        output_file=output_file,
    )
    return myget_execute(params, execution)


__all__ = [
    "MYGET_METADATA",
    "MygetOutputs",
    "MygetParameters",
    "myget",
    "myget_params",
]
