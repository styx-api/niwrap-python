# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SYNTHMORPH_METADATA = Metadata(
    id="f0911d5ad2691342f07a7e7dd405c71574415a65.boutiques",
    name="mri_synthmorph",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriSynthmorphParameters = typing.TypedDict('MriSynthmorphParameters', {
    "__STYX_TYPE__": typing.Literal["mri_synthmorph"],
    "moving_image": InputPathType,
    "fixed_image": InputPathType,
    "moved_output": typing.NotRequired[str | None],
    "transform_output": typing.NotRequired[InputPathType | None],
    "header_only": bool,
    "transformation_model": typing.NotRequired[typing.Literal["deform", "affine", "rigid"] | None],
    "init_transform": typing.NotRequired[InputPathType | None],
    "threads": typing.NotRequired[float | None],
    "gpu_flag": bool,
    "smooth": typing.NotRequired[float | None],
    "extent": typing.NotRequired[float | None],
    "model_weights": typing.NotRequired[InputPathType | None],
    "inspect_directory": typing.NotRequired[str | None],
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
        "mri_synthmorph": mri_synthmorph_cargs,
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
        "mri_synthmorph": mri_synthmorph_outputs,
    }.get(t)


class MriSynthmorphOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_synthmorph(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    moved_output_file: OutputPathType | None
    """The registered output image file, resulting from the operation."""
    transform_output_file: OutputPathType
    """Transform file resulting from registration."""


def mri_synthmorph_params(
    moving_image: InputPathType,
    fixed_image: InputPathType,
    moved_output: str | None = None,
    transform_output: InputPathType | None = None,
    header_only: bool = False,
    transformation_model: typing.Literal["deform", "affine", "rigid"] | None = "deform",
    init_transform: InputPathType | None = None,
    threads: float | None = None,
    gpu_flag: bool = False,
    smooth: float | None = 1,
    extent: float | None = 256,
    model_weights: InputPathType | None = None,
    inspect_directory: str | None = None,
) -> MriSynthmorphParameters:
    """
    Build parameters.
    
    Args:
        moving_image: The moving input image, which will be registered to the\
            fixed image.
        fixed_image: The fixed input image, which is used as the reference for\
            registration.
        moved_output: The resulting image after registration.
        transform_output: Output transform file for registration. Can be a text\
            file for linear or an image file for deformable registration.
        header_only: Adjust the voxel-to-world matrix instead of resampling.\
            Linear registration only.
        transformation_model: Specifies the registration transformation model.\
            Options include 'deform', 'affine', and 'rigid'.
        init_transform: Initial linear transform for registration.
        threads: Number of TensorFlow threads to utilize. Defaults to the\
            number of cores.
        gpu_flag: Utilize the GPU specified by CUDA_VISIBLE_DEVICES or GPU 0 if\
            unset or empty.
        smooth: Regularization parameter for deformable registration. Higher\
            values indicate smoother displacement fields.
        extent: Isotropic extent of the registration space in unit voxels.
        model_weights: Alternative model weights as an H5 file.
        inspect_directory: Save model inputs resampled into network space for\
            inspection.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_synthmorph",
        "moving_image": moving_image,
        "fixed_image": fixed_image,
        "header_only": header_only,
        "gpu_flag": gpu_flag,
    }
    if moved_output is not None:
        params["moved_output"] = moved_output
    if transform_output is not None:
        params["transform_output"] = transform_output
    if transformation_model is not None:
        params["transformation_model"] = transformation_model
    if init_transform is not None:
        params["init_transform"] = init_transform
    if threads is not None:
        params["threads"] = threads
    if smooth is not None:
        params["smooth"] = smooth
    if extent is not None:
        params["extent"] = extent
    if model_weights is not None:
        params["model_weights"] = model_weights
    if inspect_directory is not None:
        params["inspect_directory"] = inspect_directory
    return params


def mri_synthmorph_cargs(
    params: MriSynthmorphParameters,
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
    cargs.append("mri_synthmorph")
    cargs.append(execution.input_file(params.get("moving_image")))
    cargs.append(execution.input_file(params.get("fixed_image")))
    if params.get("moved_output") is not None:
        cargs.extend([
            "-o",
            params.get("moved_output")
        ])
    if params.get("transform_output") is not None:
        cargs.extend([
            "-t",
            execution.input_file(params.get("transform_output"))
        ])
    if params.get("header_only"):
        cargs.append("-H")
    if params.get("transformation_model") is not None:
        cargs.extend([
            "-m",
            params.get("transformation_model")
        ])
    if params.get("init_transform") is not None:
        cargs.extend([
            "-i",
            execution.input_file(params.get("init_transform"))
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "-j",
            str(params.get("threads"))
        ])
    if params.get("gpu_flag"):
        cargs.append("-g")
    if params.get("smooth") is not None:
        cargs.extend([
            "-s",
            str(params.get("smooth"))
        ])
    if params.get("extent") is not None:
        cargs.extend([
            "-e",
            str(params.get("extent"))
        ])
    if params.get("model_weights") is not None:
        cargs.extend([
            "-w",
            execution.input_file(params.get("model_weights"))
        ])
    if params.get("inspect_directory") is not None:
        cargs.extend([
            "--inspect",
            params.get("inspect_directory")
        ])
    return cargs


def mri_synthmorph_outputs(
    params: MriSynthmorphParameters,
    execution: Execution,
) -> MriSynthmorphOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSynthmorphOutputs(
        root=execution.output_file("."),
        moved_output_file=execution.output_file(params.get("moved_output")) if (params.get("moved_output") is not None) else None,
        transform_output_file=execution.output_file("[TRANS_OUTPUT]"),
    )
    return ret


def mri_synthmorph_execute(
    params: MriSynthmorphParameters,
    execution: Execution,
) -> MriSynthmorphOutputs:
    """
    SynthMorph is a deep-learning tool for brain-specific MRI image registration
    without preprocessing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSynthmorphOutputs`).
    """
    params = execution.params(params)
    cargs = mri_synthmorph_cargs(params, execution)
    ret = mri_synthmorph_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_synthmorph(
    moving_image: InputPathType,
    fixed_image: InputPathType,
    moved_output: str | None = None,
    transform_output: InputPathType | None = None,
    header_only: bool = False,
    transformation_model: typing.Literal["deform", "affine", "rigid"] | None = "deform",
    init_transform: InputPathType | None = None,
    threads: float | None = None,
    gpu_flag: bool = False,
    smooth: float | None = 1,
    extent: float | None = 256,
    model_weights: InputPathType | None = None,
    inspect_directory: str | None = None,
    runner: Runner | None = None,
) -> MriSynthmorphOutputs:
    """
    SynthMorph is a deep-learning tool for brain-specific MRI image registration
    without preprocessing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        moving_image: The moving input image, which will be registered to the\
            fixed image.
        fixed_image: The fixed input image, which is used as the reference for\
            registration.
        moved_output: The resulting image after registration.
        transform_output: Output transform file for registration. Can be a text\
            file for linear or an image file for deformable registration.
        header_only: Adjust the voxel-to-world matrix instead of resampling.\
            Linear registration only.
        transformation_model: Specifies the registration transformation model.\
            Options include 'deform', 'affine', and 'rigid'.
        init_transform: Initial linear transform for registration.
        threads: Number of TensorFlow threads to utilize. Defaults to the\
            number of cores.
        gpu_flag: Utilize the GPU specified by CUDA_VISIBLE_DEVICES or GPU 0 if\
            unset or empty.
        smooth: Regularization parameter for deformable registration. Higher\
            values indicate smoother displacement fields.
        extent: Isotropic extent of the registration space in unit voxels.
        model_weights: Alternative model weights as an H5 file.
        inspect_directory: Save model inputs resampled into network space for\
            inspection.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSynthmorphOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SYNTHMORPH_METADATA)
    params = mri_synthmorph_params(
        moving_image=moving_image,
        fixed_image=fixed_image,
        moved_output=moved_output,
        transform_output=transform_output,
        header_only=header_only,
        transformation_model=transformation_model,
        init_transform=init_transform,
        threads=threads,
        gpu_flag=gpu_flag,
        smooth=smooth,
        extent=extent,
        model_weights=model_weights,
        inspect_directory=inspect_directory,
    )
    return mri_synthmorph_execute(params, execution)


__all__ = [
    "MRI_SYNTHMORPH_METADATA",
    "MriSynthmorphOutputs",
    "MriSynthmorphParameters",
    "mri_synthmorph",
    "mri_synthmorph_params",
]
