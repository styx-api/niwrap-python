# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_MASK_TO_ASCII_METADATA = Metadata(
    id="778a8402c86f1b42b01b3553f5a5396f990949e6.boutiques",
    name="3dMaskToASCII",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dMaskToAsciiParameters = typing.TypedDict('V3dMaskToAsciiParameters', {
    "__STYXTYPE__": typing.Literal["3dMaskToASCII"],
    "tobin_flag": bool,
    "dataset": InputPathType,
    "outputfile": str,
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
        "3dMaskToASCII": v_3d_mask_to_ascii_cargs,
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
        "3dMaskToASCII": v_3d_mask_to_ascii_outputs,
    }.get(t)


class V3dMaskToAsciiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_mask_to_ascii(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outputfile: OutputPathType
    """Output file where ASCII string mask or binary mask will be written."""


def v_3d_mask_to_ascii_params(
    dataset: InputPathType,
    outputfile: str,
    tobin_flag: bool = False,
) -> V3dMaskToAsciiParameters:
    """
    Build parameters.
    
    Args:
        dataset: Input dataset (e.g. mask.nii.gz).
        outputfile: Output file where ASCII string mask or binary mask will be\
            written.
        tobin_flag: Read ASCII mask, expand it to byte-valued dataset, and\
            write to stdout.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dMaskToASCII",
        "tobin_flag": tobin_flag,
        "dataset": dataset,
        "outputfile": outputfile,
    }
    return params


def v_3d_mask_to_ascii_cargs(
    params: V3dMaskToAsciiParameters,
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
    cargs.append("3dMaskToASCII")
    if params.get("tobin_flag"):
        cargs.append("-tobin")
    cargs.append(execution.input_file(params.get("dataset")))
    cargs.append("> " + params.get("outputfile"))
    return cargs


def v_3d_mask_to_ascii_outputs(
    params: V3dMaskToAsciiParameters,
    execution: Execution,
) -> V3dMaskToAsciiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dMaskToAsciiOutputs(
        root=execution.output_file("."),
        outputfile=execution.output_file(params.get("outputfile")),
    )
    return ret


def v_3d_mask_to_ascii_execute(
    params: V3dMaskToAsciiParameters,
    execution: Execution,
) -> V3dMaskToAsciiOutputs:
    """
    Converts a byte-valued 0/1 dataset into an ASCII string, or vice versa.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dMaskToAsciiOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_mask_to_ascii_cargs(params, execution)
    ret = v_3d_mask_to_ascii_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_mask_to_ascii(
    dataset: InputPathType,
    outputfile: str,
    tobin_flag: bool = False,
    runner: Runner | None = None,
) -> V3dMaskToAsciiOutputs:
    """
    Converts a byte-valued 0/1 dataset into an ASCII string, or vice versa.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input dataset (e.g. mask.nii.gz).
        outputfile: Output file where ASCII string mask or binary mask will be\
            written.
        tobin_flag: Read ASCII mask, expand it to byte-valued dataset, and\
            write to stdout.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMaskToAsciiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MASK_TO_ASCII_METADATA)
    params = v_3d_mask_to_ascii_params(
        tobin_flag=tobin_flag,
        dataset=dataset,
        outputfile=outputfile,
    )
    return v_3d_mask_to_ascii_execute(params, execution)


__all__ = [
    "V3dMaskToAsciiOutputs",
    "V3dMaskToAsciiParameters",
    "V_3D_MASK_TO_ASCII_METADATA",
    "v_3d_mask_to_ascii",
    "v_3d_mask_to_ascii_params",
]
