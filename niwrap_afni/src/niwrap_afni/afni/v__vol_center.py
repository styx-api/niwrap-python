# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__VOL_CENTER_METADATA = Metadata(
    id="4ce13662130110b3fd50b4a405a5d296faf47380.boutiques",
    name="@VolCenter",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VVolCenterParameters = typing.TypedDict('VVolCenterParameters', {
    "__STYXTYPE__": typing.Literal["@VolCenter"],
    "dset": InputPathType,
    "orient": typing.NotRequired[str | None],
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
        "@VolCenter": v__vol_center_cargs,
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


class VVolCenterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__vol_center(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__vol_center_params(
    dset: InputPathType,
    orient: str | None = None,
) -> VVolCenterParameters:
    """
    Build parameters.
    
    Args:
        dset: Input volume dataset.
        orient: Output coordinate system orientation (e.g., RAI).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@VolCenter",
        "dset": dset,
    }
    if orient is not None:
        params["orient"] = orient
    return params


def v__vol_center_cargs(
    params: VVolCenterParameters,
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
    cargs.append("@VolCenter")
    cargs.extend([
        "-dset",
        execution.input_file(params.get("dset"))
    ])
    if params.get("orient") is not None:
        cargs.extend([
            "-or",
            params.get("orient")
        ])
    return cargs


def v__vol_center_outputs(
    params: VVolCenterParameters,
    execution: Execution,
) -> VVolCenterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VVolCenterOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__vol_center_execute(
    params: VVolCenterParameters,
    execution: Execution,
) -> VVolCenterOutputs:
    """
    Tool to return the center of volume for a given dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VVolCenterOutputs`).
    """
    params = execution.params(params)
    cargs = v__vol_center_cargs(params, execution)
    ret = v__vol_center_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__vol_center(
    dset: InputPathType,
    orient: str | None = None,
    runner: Runner | None = None,
) -> VVolCenterOutputs:
    """
    Tool to return the center of volume for a given dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dset: Input volume dataset.
        orient: Output coordinate system orientation (e.g., RAI).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VVolCenterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__VOL_CENTER_METADATA)
    params = v__vol_center_params(
        dset=dset,
        orient=orient,
    )
    return v__vol_center_execute(params, execution)


__all__ = [
    "VVolCenterOutputs",
    "VVolCenterParameters",
    "V__VOL_CENTER_METADATA",
    "v__vol_center",
    "v__vol_center_params",
]
