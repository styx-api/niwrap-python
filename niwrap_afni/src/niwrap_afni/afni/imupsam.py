# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMUPSAM_METADATA = Metadata(
    id="d769dae1e4c21af6509b731daf0c2ab2e1688ccf.boutiques",
    name="imupsam",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


ImupsamParameters = typing.TypedDict('ImupsamParameters', {
    "__STYX_TYPE__": typing.Literal["imupsam"],
    "ascii_flag": bool,
    "factor": int,
    "input_image": InputPathType,
    "output_image": str,
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
        "imupsam": imupsam_cargs,
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
        "imupsam": imupsam_outputs,
    }.get(t)


class ImupsamOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imupsam(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType
    """Upsampled image output file"""


def imupsam_params(
    factor: int,
    input_image: InputPathType,
    output_image: str,
    ascii_flag: bool = False,
) -> ImupsamParameters:
    """
    Build parameters.
    
    Args:
        factor: Upsampling factor; must be an integer in the range 2 to 30.
        input_image: Path of the input 2D image file.
        output_image: Path of the output upsampled image file. Use '-' to write\
            to stdout.
        ascii_flag: Write the result in ASCII format: all numbers for the file\
            are output, with no header info.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "imupsam",
        "ascii_flag": ascii_flag,
        "factor": factor,
        "input_image": input_image,
        "output_image": output_image,
    }
    return params


def imupsam_cargs(
    params: ImupsamParameters,
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
    cargs.append("imupsam")
    if params.get("ascii_flag"):
        cargs.append("-A")
    cargs.append(str(params.get("factor")))
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_image"))
    return cargs


def imupsam_outputs(
    params: ImupsamParameters,
    execution: Execution,
) -> ImupsamOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ImupsamOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(params.get("output_image")),
    )
    return ret


def imupsam_execute(
    params: ImupsamParameters,
    execution: Execution,
) -> ImupsamOutputs:
    """
    Upsamples a 2D image by a specified factor.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ImupsamOutputs`).
    """
    params = execution.params(params)
    cargs = imupsam_cargs(params, execution)
    ret = imupsam_outputs(params, execution)
    execution.run(cargs)
    return ret


def imupsam(
    factor: int,
    input_image: InputPathType,
    output_image: str,
    ascii_flag: bool = False,
    runner: Runner | None = None,
) -> ImupsamOutputs:
    """
    Upsamples a 2D image by a specified factor.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        factor: Upsampling factor; must be an integer in the range 2 to 30.
        input_image: Path of the input 2D image file.
        output_image: Path of the output upsampled image file. Use '-' to write\
            to stdout.
        ascii_flag: Write the result in ASCII format: all numbers for the file\
            are output, with no header info.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImupsamOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMUPSAM_METADATA)
    params = imupsam_params(
        ascii_flag=ascii_flag,
        factor=factor,
        input_image=input_image,
        output_image=output_image,
    )
    return imupsam_execute(params, execution)


__all__ = [
    "IMUPSAM_METADATA",
    "ImupsamOutputs",
    "ImupsamParameters",
    "imupsam",
    "imupsam_params",
]
