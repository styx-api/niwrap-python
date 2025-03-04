# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_POLV_METADATA = Metadata(
    id="ee8644189f031978bc3740be0222cfee554fee9b.boutiques",
    name="mri_polv",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriPolvParameters = typing.TypedDict('MriPolvParameters', {
    "__STYX_TYPE__": typing.Literal["mri_polv"],
    "window_size": typing.NotRequired[float | None],
    "input_image": InputPathType,
    "output_image": InputPathType,
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
        "mri_polv": mri_polv_cargs,
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


class MriPolvOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_polv(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_polv_params(
    input_image: InputPathType,
    output_image: InputPathType,
    window_size: float | None = None,
) -> MriPolvParameters:
    """
    Build parameters.
    
    Args:
        input_image: The input image file for processing.
        output_image: The output image file specifying the plane of least\
            variance.
        window_size: Specify the window size to be used in the calculation of\
            the central plane of least variance (default=5).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_polv",
        "input_image": input_image,
        "output_image": output_image,
    }
    if window_size is not None:
        params["window_size"] = window_size
    return params


def mri_polv_cargs(
    params: MriPolvParameters,
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
    cargs.append("mri_polv")
    if params.get("window_size") is not None:
        cargs.extend([
            "-w",
            str(params.get("window_size"))
        ])
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(execution.input_file(params.get("output_image")))
    return cargs


def mri_polv_outputs(
    params: MriPolvParameters,
    execution: Execution,
) -> MriPolvOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriPolvOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_polv_execute(
    params: MriPolvParameters,
    execution: Execution,
) -> MriPolvOutputs:
    """
    Calculate an image specifying the plane of least variance at each point in the
    input image.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriPolvOutputs`).
    """
    params = execution.params(params)
    cargs = mri_polv_cargs(params, execution)
    ret = mri_polv_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_polv(
    input_image: InputPathType,
    output_image: InputPathType,
    window_size: float | None = None,
    runner: Runner | None = None,
) -> MriPolvOutputs:
    """
    Calculate an image specifying the plane of least variance at each point in the
    input image.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: The input image file for processing.
        output_image: The output image file specifying the plane of least\
            variance.
        window_size: Specify the window size to be used in the calculation of\
            the central plane of least variance (default=5).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriPolvOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_POLV_METADATA)
    params = mri_polv_params(
        window_size=window_size,
        input_image=input_image,
        output_image=output_image,
    )
    return mri_polv_execute(params, execution)


__all__ = [
    "MRI_POLV_METADATA",
    "MriPolvOutputs",
    "MriPolvParameters",
    "mri_polv",
    "mri_polv_params",
]
