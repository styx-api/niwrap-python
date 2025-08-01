# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_GETROW_METADATA = Metadata(
    id="07f583964934ab4d2f12cc2751f27623c441a893.boutiques",
    name="3dGetrow",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dGetrowParameters = typing.TypedDict('V3dGetrowParameters', {
    "__STYXTYPE__": typing.Literal["3dGetrow"],
    "xrow": typing.NotRequired[list[int] | None],
    "yrow": typing.NotRequired[list[int] | None],
    "zrow": typing.NotRequired[list[int] | None],
    "input_file": typing.NotRequired[InputPathType | None],
    "output_file": typing.NotRequired[str | None],
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
        "3dGetrow": v_3d_getrow_cargs,
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
        "3dGetrow": v_3d_getrow_outputs,
    }.get(t)


class V3dGetrowOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_getrow(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Output .1D ASCII file"""


def v_3d_getrow_params(
    xrow: list[int] | None = None,
    yrow: list[int] | None = None,
    zrow: list[int] | None = None,
    input_file: InputPathType | None = None,
    output_file: str | None = None,
) -> V3dGetrowParameters:
    """
    Build parameters.
    
    Args:
        xrow: Extract row along the x-direction at fixed y-index of j and fixed\
            z-index of k.
        yrow: Extract row along the y-direction at fixed x-index of i and fixed\
            z-index of k.
        zrow: Extract row along the z-direction at fixed x-index of i and fixed\
            y-index of j.
        input_file: Read input from dataset 'ddd' (instead of putting dataset\
            name at end of command line).
        output_file: Filename for output .1D ASCII file will be 'ff' (if 'ff'\
            is '-', then output is to stdout, the default).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dGetrow",
    }
    if xrow is not None:
        params["xrow"] = xrow
    if yrow is not None:
        params["yrow"] = yrow
    if zrow is not None:
        params["zrow"] = zrow
    if input_file is not None:
        params["input_file"] = input_file
    if output_file is not None:
        params["output_file"] = output_file
    return params


def v_3d_getrow_cargs(
    params: V3dGetrowParameters,
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
    cargs.append("3dGetrow")
    if params.get("xrow") is not None:
        cargs.extend([
            "-xrow",
            *map(str, params.get("xrow"))
        ])
    if params.get("yrow") is not None:
        cargs.extend([
            "-yrow",
            *map(str, params.get("yrow"))
        ])
    if params.get("zrow") is not None:
        cargs.extend([
            "-zrow",
            *map(str, params.get("zrow"))
        ])
    if params.get("input_file") is not None:
        cargs.extend([
            "-input",
            execution.input_file(params.get("input_file"))
        ])
    if params.get("output_file") is not None:
        cargs.extend([
            "-output",
            params.get("output_file")
        ])
    return cargs


def v_3d_getrow_outputs(
    params: V3dGetrowParameters,
    execution: Execution,
) -> V3dGetrowOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dGetrowOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(params.get("output_file") + ".1D") if (params.get("output_file") is not None) else None,
    )
    return ret


def v_3d_getrow_execute(
    params: V3dGetrowParameters,
    execution: Execution,
) -> V3dGetrowOutputs:
    """
    Program to extract 1 row from a dataset and write it as a .1D file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dGetrowOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_getrow_cargs(params, execution)
    ret = v_3d_getrow_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_getrow(
    xrow: list[int] | None = None,
    yrow: list[int] | None = None,
    zrow: list[int] | None = None,
    input_file: InputPathType | None = None,
    output_file: str | None = None,
    runner: Runner | None = None,
) -> V3dGetrowOutputs:
    """
    Program to extract 1 row from a dataset and write it as a .1D file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        xrow: Extract row along the x-direction at fixed y-index of j and fixed\
            z-index of k.
        yrow: Extract row along the y-direction at fixed x-index of i and fixed\
            z-index of k.
        zrow: Extract row along the z-direction at fixed x-index of i and fixed\
            y-index of j.
        input_file: Read input from dataset 'ddd' (instead of putting dataset\
            name at end of command line).
        output_file: Filename for output .1D ASCII file will be 'ff' (if 'ff'\
            is '-', then output is to stdout, the default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dGetrowOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_GETROW_METADATA)
    params = v_3d_getrow_params(
        xrow=xrow,
        yrow=yrow,
        zrow=zrow,
        input_file=input_file,
        output_file=output_file,
    )
    return v_3d_getrow_execute(params, execution)


__all__ = [
    "V3dGetrowOutputs",
    "V3dGetrowParameters",
    "V_3D_GETROW_METADATA",
    "v_3d_getrow",
    "v_3d_getrow_params",
]
