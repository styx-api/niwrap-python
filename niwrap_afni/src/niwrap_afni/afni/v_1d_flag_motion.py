# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_1D_FLAG_MOTION_METADATA = Metadata(
    id="efc64bd39dbf6f50e88a48eb1a0be3834e4162f6.boutiques",
    name="1dFlagMotion",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V1dFlagMotionParameters = typing.TypedDict('V1dFlagMotionParameters', {
    "__STYX_TYPE__": typing.Literal["1dFlagMotion"],
    "input_motion_file": InputPathType,
    "max_translation": typing.NotRequired[float | None],
    "max_rotation": typing.NotRequired[float | None],
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
        "1dFlagMotion": v_1d_flag_motion_cargs,
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
        "1dFlagMotion": v_1d_flag_motion_outputs,
    }.get(t)


class V1dFlagMotionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_flag_motion(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_points: OutputPathType
    """List of points exceeding the motion bounds in 1D format"""


def v_1d_flag_motion_params(
    input_motion_file: InputPathType,
    max_translation: float | None = None,
    max_rotation: float | None = None,
) -> V1dFlagMotionParameters:
    """
    Build parameters.
    
    Args:
        input_motion_file: Input file with EXACTLY 6 columns: roll pitch yaw\
            delta-SI delta-LR delta-AP (angles in degrees followed by translations\
            in mm).
        max_translation: Maximum translation allowed in any direction (defaults\
            to 1.5mm).
        max_rotation: Maximum rotation allowed in any direction (defaults to\
            1.25 degrees).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dFlagMotion",
        "input_motion_file": input_motion_file,
    }
    if max_translation is not None:
        params["max_translation"] = max_translation
    if max_rotation is not None:
        params["max_rotation"] = max_rotation
    return params


def v_1d_flag_motion_cargs(
    params: V1dFlagMotionParameters,
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
    cargs.append("1dFlagMotion")
    cargs.append(execution.input_file(params.get("input_motion_file")))
    if params.get("max_translation") is not None:
        cargs.extend([
            "-MaxTrans",
            str(params.get("max_translation"))
        ])
    if params.get("max_rotation") is not None:
        cargs.extend([
            "-MaxRot",
            str(params.get("max_rotation"))
        ])
    return cargs


def v_1d_flag_motion_outputs(
    params: V1dFlagMotionParameters,
    execution: Execution,
) -> V1dFlagMotionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dFlagMotionOutputs(
        root=execution.output_file("."),
        output_points=execution.output_file("output_motion_points.1D"),
    )
    return ret


def v_1d_flag_motion_execute(
    params: V1dFlagMotionParameters,
    execution: Execution,
) -> V1dFlagMotionOutputs:
    """
    Produces a list of time points with excessive motion relative to the previous
    time point.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dFlagMotionOutputs`).
    """
    params = execution.params(params)
    cargs = v_1d_flag_motion_cargs(params, execution)
    ret = v_1d_flag_motion_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1d_flag_motion(
    input_motion_file: InputPathType,
    max_translation: float | None = None,
    max_rotation: float | None = None,
    runner: Runner | None = None,
) -> V1dFlagMotionOutputs:
    """
    Produces a list of time points with excessive motion relative to the previous
    time point.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_motion_file: Input file with EXACTLY 6 columns: roll pitch yaw\
            delta-SI delta-LR delta-AP (angles in degrees followed by translations\
            in mm).
        max_translation: Maximum translation allowed in any direction (defaults\
            to 1.5mm).
        max_rotation: Maximum rotation allowed in any direction (defaults to\
            1.25 degrees).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dFlagMotionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_FLAG_MOTION_METADATA)
    params = v_1d_flag_motion_params(
        input_motion_file=input_motion_file,
        max_translation=max_translation,
        max_rotation=max_rotation,
    )
    return v_1d_flag_motion_execute(params, execution)


__all__ = [
    "V1dFlagMotionOutputs",
    "V1dFlagMotionParameters",
    "V_1D_FLAG_MOTION_METADATA",
    "v_1d_flag_motion",
    "v_1d_flag_motion_params",
]
