# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_AFNITO_RAW_METADATA = Metadata(
    id="fbf9965fdc0f2095a41d56980e48457852926f51.boutiques",
    name="3dAFNItoRaw",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dAfnitoRawParameters = typing.TypedDict('V3dAfnitoRawParameters', {
    "__STYXTYPE__": typing.Literal["3dAFNItoRaw"],
    "output_file": typing.NotRequired[str | None],
    "force_float": bool,
    "dataset": str,
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
        "3dAFNItoRaw": v_3d_afnito_raw_cargs,
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


class V3dAfnitoRawOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_afnito_raw(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_afnito_raw_params(
    dataset: str,
    output_file: str | None = None,
    force_float: bool = False,
) -> V3dAfnitoRawParameters:
    """
    Build parameters.
    
    Args:
        dataset: Input AFNI dataset with possible modifiers for sub-brick and\
            sub-range selection.
        output_file: Name of the output file (not an AFNI dataset prefix).\
            Default is rawxyz.dat.
        force_float: Force floating point output. Floating point forced if any\
            sub-brik scale factors not equal to 1.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dAFNItoRaw",
        "force_float": force_float,
        "dataset": dataset,
    }
    if output_file is not None:
        params["output_file"] = output_file
    return params


def v_3d_afnito_raw_cargs(
    params: V3dAfnitoRawParameters,
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
    cargs.append("3dAFNItoRaw")
    if params.get("output_file") is not None:
        cargs.extend([
            "-output",
            params.get("output_file")
        ])
    if params.get("force_float"):
        cargs.append("-datum float")
    cargs.append(params.get("dataset"))
    return cargs


def v_3d_afnito_raw_outputs(
    params: V3dAfnitoRawParameters,
    execution: Execution,
) -> V3dAfnitoRawOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dAfnitoRawOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3d_afnito_raw_execute(
    params: V3dAfnitoRawParameters,
    execution: Execution,
) -> V3dAfnitoRawOutputs:
    """
    Convert an AFNI brik file with multiple sub-briks to a raw file with each
    sub-brik voxel concatenated voxel-wise.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dAfnitoRawOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_afnito_raw_cargs(params, execution)
    ret = v_3d_afnito_raw_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_afnito_raw(
    dataset: str,
    output_file: str | None = None,
    force_float: bool = False,
    runner: Runner | None = None,
) -> V3dAfnitoRawOutputs:
    """
    Convert an AFNI brik file with multiple sub-briks to a raw file with each
    sub-brik voxel concatenated voxel-wise.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input AFNI dataset with possible modifiers for sub-brick and\
            sub-range selection.
        output_file: Name of the output file (not an AFNI dataset prefix).\
            Default is rawxyz.dat.
        force_float: Force floating point output. Floating point forced if any\
            sub-brik scale factors not equal to 1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAfnitoRawOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AFNITO_RAW_METADATA)
    params = v_3d_afnito_raw_params(
        output_file=output_file,
        force_float=force_float,
        dataset=dataset,
    )
    return v_3d_afnito_raw_execute(params, execution)


__all__ = [
    "V3dAfnitoRawOutputs",
    "V3dAfnitoRawParameters",
    "V_3D_AFNITO_RAW_METADATA",
    "v_3d_afnito_raw",
    "v_3d_afnito_raw_params",
]
