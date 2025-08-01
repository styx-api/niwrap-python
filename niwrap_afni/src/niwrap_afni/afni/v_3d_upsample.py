# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_UPSAMPLE_METADATA = Metadata(
    id="1517c44535a12e8aed86c6a112d119fc406a90b4.boutiques",
    name="3dUpsample",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dUpsampleParameters = typing.TypedDict('V3dUpsampleParameters', {
    "__STYXTYPE__": typing.Literal["3dUpsample"],
    "upsample_factor": int,
    "input_dataset": str,
    "linear_interpolation": bool,
    "output_prefix": typing.NotRequired[str | None],
    "verbose_flag": bool,
    "datatype": typing.NotRequired[str | None],
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
        "3dUpsample": v_3d_upsample_cargs,
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
        "3dUpsample": v_3d_upsample_outputs,
    }.get(t)


class V3dUpsampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_upsample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brik: OutputPathType | None
    """Upsampled dataset in BRIK format."""
    output_head: OutputPathType | None
    """Header information for the upsampled dataset."""


def v_3d_upsample_params(
    upsample_factor: int,
    input_dataset: str,
    linear_interpolation: bool = False,
    output_prefix: str | None = None,
    verbose_flag: bool = False,
    datatype: str | None = None,
) -> V3dUpsampleParameters:
    """
    Build parameters.
    
    Args:
        upsample_factor: Upsampling factor; must be between 2 and 320\
            (inclusive).
        input_dataset: Input dataset.
        linear_interpolation: Use linear interpolation instead of 7th order\
            polynomial interpolation.
        output_prefix: Define the prefix name of the output dataset; default is\
            'Upsam'.
        verbose_flag: Print verbose output.
        datatype: Specify the datatype for the output dataset (float, short,\
            byte); default is float.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dUpsample",
        "upsample_factor": upsample_factor,
        "input_dataset": input_dataset,
        "linear_interpolation": linear_interpolation,
        "verbose_flag": verbose_flag,
    }
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if datatype is not None:
        params["datatype"] = datatype
    return params


def v_3d_upsample_cargs(
    params: V3dUpsampleParameters,
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
    cargs.append("3dUpsample")
    cargs.extend([
        "-n",
        str(params.get("upsample_factor"))
    ])
    cargs.extend([
        "-input",
        params.get("input_dataset")
    ])
    if params.get("linear_interpolation"):
        cargs.append("-1")
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    if params.get("verbose_flag"):
        cargs.append("-verb")
    if params.get("datatype") is not None:
        cargs.extend([
            "-datum",
            params.get("datatype")
        ])
    return cargs


def v_3d_upsample_outputs(
    params: V3dUpsampleParameters,
    execution: Execution,
) -> V3dUpsampleOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dUpsampleOutputs(
        root=execution.output_file("."),
        output_brik=execution.output_file(params.get("output_prefix") + "+orig.BRIK") if (params.get("output_prefix") is not None) else None,
        output_head=execution.output_file(params.get("output_prefix") + "+orig.HEAD") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def v_3d_upsample_execute(
    params: V3dUpsampleParameters,
    execution: Execution,
) -> V3dUpsampleOutputs:
    """
    Upsamples a 3D+time dataset in the time direction by a specified factor.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dUpsampleOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_upsample_cargs(params, execution)
    ret = v_3d_upsample_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_upsample(
    upsample_factor: int,
    input_dataset: str,
    linear_interpolation: bool = False,
    output_prefix: str | None = None,
    verbose_flag: bool = False,
    datatype: str | None = None,
    runner: Runner | None = None,
) -> V3dUpsampleOutputs:
    """
    Upsamples a 3D+time dataset in the time direction by a specified factor.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        upsample_factor: Upsampling factor; must be between 2 and 320\
            (inclusive).
        input_dataset: Input dataset.
        linear_interpolation: Use linear interpolation instead of 7th order\
            polynomial interpolation.
        output_prefix: Define the prefix name of the output dataset; default is\
            'Upsam'.
        verbose_flag: Print verbose output.
        datatype: Specify the datatype for the output dataset (float, short,\
            byte); default is float.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dUpsampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_UPSAMPLE_METADATA)
    params = v_3d_upsample_params(
        upsample_factor=upsample_factor,
        input_dataset=input_dataset,
        linear_interpolation=linear_interpolation,
        output_prefix=output_prefix,
        verbose_flag=verbose_flag,
        datatype=datatype,
    )
    return v_3d_upsample_execute(params, execution)


__all__ = [
    "V3dUpsampleOutputs",
    "V3dUpsampleParameters",
    "V_3D_UPSAMPLE_METADATA",
    "v_3d_upsample",
    "v_3d_upsample_params",
]
