# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANTS_DENOISE_IMAGE_FS_METADATA = Metadata(
    id="ceaab64d93fccf1f1155efcaaae5de0e2ed14132.boutiques",
    name="AntsDenoiseImageFs",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


AntsDenoiseImageFsParameters = typing.TypedDict('AntsDenoiseImageFsParameters', {
    "__STYXTYPE__": typing.Literal["AntsDenoiseImageFs"],
    "input_image": InputPathType,
    "output_image": str,
    "rician_flag": bool,
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
        "AntsDenoiseImageFs": ants_denoise_image_fs_cargs,
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
        "AntsDenoiseImageFs": ants_denoise_image_fs_outputs,
    }.get(t)


class AntsDenoiseImageFsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_denoise_image_fs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    denoised_output: OutputPathType
    """Resulting denoised volume file"""


def ants_denoise_image_fs_params(
    input_image: InputPathType,
    output_image: str = "output.nii",
    rician_flag: bool = False,
) -> AntsDenoiseImageFsParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input volume file.
        output_image: Denoised volume file.
        rician_flag: Enable Rician noise model (otherwise Gaussian is used).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "AntsDenoiseImageFs",
        "input_image": input_image,
        "output_image": output_image,
        "rician_flag": rician_flag,
    }
    return params


def ants_denoise_image_fs_cargs(
    params: AntsDenoiseImageFsParameters,
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
    cargs.append("AntsDenoiseImageFs")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_image"))
    ])
    cargs.extend([
        "-o",
        params.get("output_image")
    ])
    if params.get("rician_flag"):
        cargs.append("--rician")
    return cargs


def ants_denoise_image_fs_outputs(
    params: AntsDenoiseImageFsParameters,
    execution: Execution,
) -> AntsDenoiseImageFsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsDenoiseImageFsOutputs(
        root=execution.output_file("."),
        denoised_output=execution.output_file(params.get("output_image")),
    )
    return ret


def ants_denoise_image_fs_execute(
    params: AntsDenoiseImageFsParameters,
    execution: Execution,
) -> AntsDenoiseImageFsOutputs:
    """
    Denoises an image with a spatially adaptive filter. This program wraps the
    AntsDenoiseImage utility available in the ANTs package.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsDenoiseImageFsOutputs`).
    """
    params = execution.params(params)
    cargs = ants_denoise_image_fs_cargs(params, execution)
    ret = ants_denoise_image_fs_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_denoise_image_fs(
    input_image: InputPathType,
    output_image: str = "output.nii",
    rician_flag: bool = False,
    runner: Runner | None = None,
) -> AntsDenoiseImageFsOutputs:
    """
    Denoises an image with a spatially adaptive filter. This program wraps the
    AntsDenoiseImage utility available in the ANTs package.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: Input volume file.
        output_image: Denoised volume file.
        rician_flag: Enable Rician noise model (otherwise Gaussian is used).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsDenoiseImageFsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_DENOISE_IMAGE_FS_METADATA)
    params = ants_denoise_image_fs_params(
        input_image=input_image,
        output_image=output_image,
        rician_flag=rician_flag,
    )
    return ants_denoise_image_fs_execute(params, execution)


__all__ = [
    "ANTS_DENOISE_IMAGE_FS_METADATA",
    "AntsDenoiseImageFsOutputs",
    "AntsDenoiseImageFsParameters",
    "ants_denoise_image_fs",
    "ants_denoise_image_fs_params",
]
