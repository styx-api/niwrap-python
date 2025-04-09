# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DENOISE_IMAGE_METADATA = Metadata(
    id="c724dafafc43426f15d57c46a1fd25866000d279.boutiques",
    name="DenoiseImage",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


DenoiseImageCorrectedOutputParameters = typing.TypedDict('DenoiseImageCorrectedOutputParameters', {
    "__STYX_TYPE__": typing.Literal["correctedOutput"],
    "correctedOutputFileName": str,
})


DenoiseImageCorrectedOutputNoiseParameters = typing.TypedDict('DenoiseImageCorrectedOutputNoiseParameters', {
    "__STYX_TYPE__": typing.Literal["correctedOutputNoise"],
    "correctedOutputFileName": str,
    "noiseFile": typing.NotRequired[str | None],
})


DenoiseImageParameters = typing.TypedDict('DenoiseImageParameters', {
    "__STYX_TYPE__": typing.Literal["DenoiseImage"],
    "image_dimensionality": typing.NotRequired[typing.Literal[2, 3, 4] | None],
    "noise_model": typing.NotRequired[typing.Literal["Gaussian", "Rician"] | None],
    "shrink_factor": typing.NotRequired[int | None],
    "mask_image": typing.NotRequired[InputPathType | None],
    "patch_radius": typing.NotRequired[str | None],
    "search_radius": typing.NotRequired[str | None],
    "verbose": typing.NotRequired[typing.Literal[0, 1] | None],
    "input_image": InputPathType,
    "output": typing.Union[DenoiseImageCorrectedOutputParameters, DenoiseImageCorrectedOutputNoiseParameters],
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
        "DenoiseImage": denoise_image_cargs,
        "correctedOutput": denoise_image_corrected_output_cargs,
        "correctedOutputNoise": denoise_image_corrected_output_noise_cargs,
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
        "DenoiseImage": denoise_image_outputs,
        "correctedOutput": denoise_image_corrected_output_outputs,
        "correctedOutputNoise": denoise_image_corrected_output_noise_outputs,
    }.get(t)


class DenoiseImageCorrectedOutputOutputs(typing.NamedTuple):
    """
    Output object returned when calling `DenoiseImageCorrectedOutputParameters(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_outfile: OutputPathType
    """Denoised image."""


def denoise_image_corrected_output_params(
    corrected_output_file_name: str,
) -> DenoiseImageCorrectedOutputParameters:
    """
    Build parameters.
    
    Args:
        corrected_output_file_name: Output file name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "correctedOutput",
        "correctedOutputFileName": corrected_output_file_name,
    }
    return params


def denoise_image_corrected_output_cargs(
    params: DenoiseImageCorrectedOutputParameters,
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
    cargs.append(params.get("correctedOutputFileName"))
    return cargs


def denoise_image_corrected_output_outputs(
    params: DenoiseImageCorrectedOutputParameters,
    execution: Execution,
) -> DenoiseImageCorrectedOutputOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DenoiseImageCorrectedOutputOutputs(
        root=execution.output_file("."),
        output_image_outfile=execution.output_file(params.get("correctedOutputFileName")),
    )
    return ret


class DenoiseImageCorrectedOutputNoiseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `DenoiseImageCorrectedOutputNoiseParameters(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_outfile: OutputPathType
    """Denoised output image."""
    output_bias_image: OutputPathType | None
    """Noise map image."""


def denoise_image_corrected_output_noise_params(
    corrected_output_file_name: str,
    noise_file: str | None = None,
) -> DenoiseImageCorrectedOutputNoiseParameters:
    """
    Build parameters.
    
    Args:
        corrected_output_file_name: Output file name.
        noise_file: Output noise map image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "correctedOutputNoise",
        "correctedOutputFileName": corrected_output_file_name,
    }
    if noise_file is not None:
        params["noiseFile"] = noise_file
    return params


def denoise_image_corrected_output_noise_cargs(
    params: DenoiseImageCorrectedOutputNoiseParameters,
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
    if params.get("noiseFile") is not None:
        cargs.append("[" + params.get("correctedOutputFileName") + "," + params.get("noiseFile") + "]")
    return cargs


def denoise_image_corrected_output_noise_outputs(
    params: DenoiseImageCorrectedOutputNoiseParameters,
    execution: Execution,
) -> DenoiseImageCorrectedOutputNoiseOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DenoiseImageCorrectedOutputNoiseOutputs(
        root=execution.output_file("."),
        output_image_outfile=execution.output_file(params.get("correctedOutputFileName")),
        output_bias_image=execution.output_file(params.get("noiseFile")) if (params.get("noiseFile") is not None) else None,
    )
    return ret


class DenoiseImageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `denoise_image(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: typing.Union[DenoiseImageCorrectedOutputOutputs, DenoiseImageCorrectedOutputNoiseOutputs]
    """Outputs from `DenoiseImageCorrectedOutputParameters` or
    `DenoiseImageCorrectedOutputNoiseParameters`."""


def denoise_image_params(
    input_image: InputPathType,
    output: typing.Union[DenoiseImageCorrectedOutputParameters, DenoiseImageCorrectedOutputNoiseParameters],
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    noise_model: typing.Literal["Gaussian", "Rician"] | None = None,
    shrink_factor: int | None = None,
    mask_image: InputPathType | None = None,
    patch_radius: str | None = None,
    search_radius: str | None = None,
    verbose: typing.Literal[0, 1] | None = None,
) -> DenoiseImageParameters:
    """
    Build parameters.
    
    Args:
        input_image: -i, --input-image inputImageFilename. A scalar image is\
            expected as input for noise correction.
        output: The denoised version of the input image, with optional noise\
            map image.
        image_dimensionality: -d, --image-dimensionality 2/3/4. This option\
            forces the image to be treated as a specified-dimensional image. If not\
            specified, the program tries to infer the dimensionality from the input\
            image.
        noise_model: -n, --noise-model Rician/(Gaussian). Employ a Rician or\
            Gaussian noise model.
        shrink_factor: -s, --shrink-factor (1)/2/3/... Running noise correction\
            on large images can be time consuming. To lessen computation time, the\
            input image can be resampled. The shrink factor, specified as a single\
            integer, describes this resampling. Shrink factor = 1 is the default.
        mask_image: -x, --mask-image maskImageFilename. If a mask image is\
            specified, denoising is only performed in the mask region.
        patch_radius: -p, --patch-radius 1x1x1. Patch radius. Default is 1x1x1.
        search_radius: -r, --search-radius 2x2x2. Search radius. Default is\
            2x2x2.
        verbose: Verbose output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "DenoiseImage",
        "input_image": input_image,
        "output": output,
    }
    if image_dimensionality is not None:
        params["image_dimensionality"] = image_dimensionality
    if noise_model is not None:
        params["noise_model"] = noise_model
    if shrink_factor is not None:
        params["shrink_factor"] = shrink_factor
    if mask_image is not None:
        params["mask_image"] = mask_image
    if patch_radius is not None:
        params["patch_radius"] = patch_radius
    if search_radius is not None:
        params["search_radius"] = search_radius
    if verbose is not None:
        params["verbose"] = verbose
    return params


def denoise_image_cargs(
    params: DenoiseImageParameters,
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
    cargs.append("DenoiseImage")
    if params.get("image_dimensionality") is not None:
        cargs.extend([
            "--image-dimensionality",
            str(params.get("image_dimensionality"))
        ])
    if params.get("noise_model") is not None:
        cargs.extend([
            "--noise-model",
            params.get("noise_model")
        ])
    if params.get("shrink_factor") is not None:
        cargs.extend([
            "--shrink-factor",
            str(params.get("shrink_factor"))
        ])
    if params.get("mask_image") is not None:
        cargs.extend([
            "--mask-image",
            execution.input_file(params.get("mask_image"))
        ])
    if params.get("patch_radius") is not None:
        cargs.extend([
            "--patch-radius",
            params.get("patch_radius")
        ])
    if params.get("search_radius") is not None:
        cargs.extend([
            "--search-radius",
            params.get("search_radius")
        ])
    if params.get("verbose") is not None:
        cargs.extend([
            "--verbose",
            str(params.get("verbose"))
        ])
    cargs.extend([
        "--input-image",
        execution.input_file(params.get("input_image"))
    ])
    cargs.extend([
        "--output",
        *dyn_cargs(params.get("output")["__STYXTYPE__"])(params.get("output"), execution)
    ])
    return cargs


def denoise_image_outputs(
    params: DenoiseImageParameters,
    execution: Execution,
) -> DenoiseImageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DenoiseImageOutputs(
        root=execution.output_file("."),
        output=dyn_outputs(params.get("output")["__STYXTYPE__"])(params.get("output"), execution),
    )
    return ret


def denoise_image_execute(
    params: DenoiseImageParameters,
    execution: Execution,
) -> DenoiseImageOutputs:
    """
    Denoise an image using a spatially adaptive filter originally described in J. V.
    Manjon, P. Coupe, Luis Marti-Bonmati, D. L. Collins, and M. Robles. Adaptive
    Non-Local Means Denoising of MR Images With Spatially Varying Noise Levels,
    Journal of Magnetic Resonance Imaging, 31:192-203, June 2010.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DenoiseImageOutputs`).
    """
    params = execution.params(params)
    cargs = denoise_image_cargs(params, execution)
    ret = denoise_image_outputs(params, execution)
    execution.run(cargs)
    return ret


def denoise_image(
    input_image: InputPathType,
    output: typing.Union[DenoiseImageCorrectedOutputParameters, DenoiseImageCorrectedOutputNoiseParameters],
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    noise_model: typing.Literal["Gaussian", "Rician"] | None = None,
    shrink_factor: int | None = None,
    mask_image: InputPathType | None = None,
    patch_radius: str | None = None,
    search_radius: str | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    runner: Runner | None = None,
) -> DenoiseImageOutputs:
    """
    Denoise an image using a spatially adaptive filter originally described in J. V.
    Manjon, P. Coupe, Luis Marti-Bonmati, D. L. Collins, and M. Robles. Adaptive
    Non-Local Means Denoising of MR Images With Spatially Varying Noise Levels,
    Journal of Magnetic Resonance Imaging, 31:192-203, June 2010.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        input_image: -i, --input-image inputImageFilename. A scalar image is\
            expected as input for noise correction.
        output: The denoised version of the input image, with optional noise\
            map image.
        image_dimensionality: -d, --image-dimensionality 2/3/4. This option\
            forces the image to be treated as a specified-dimensional image. If not\
            specified, the program tries to infer the dimensionality from the input\
            image.
        noise_model: -n, --noise-model Rician/(Gaussian). Employ a Rician or\
            Gaussian noise model.
        shrink_factor: -s, --shrink-factor (1)/2/3/... Running noise correction\
            on large images can be time consuming. To lessen computation time, the\
            input image can be resampled. The shrink factor, specified as a single\
            integer, describes this resampling. Shrink factor = 1 is the default.
        mask_image: -x, --mask-image maskImageFilename. If a mask image is\
            specified, denoising is only performed in the mask region.
        patch_radius: -p, --patch-radius 1x1x1. Patch radius. Default is 1x1x1.
        search_radius: -r, --search-radius 2x2x2. Search radius. Default is\
            2x2x2.
        verbose: Verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DenoiseImageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DENOISE_IMAGE_METADATA)
    params = denoise_image_params(
        image_dimensionality=image_dimensionality,
        noise_model=noise_model,
        shrink_factor=shrink_factor,
        mask_image=mask_image,
        patch_radius=patch_radius,
        search_radius=search_radius,
        verbose=verbose,
        input_image=input_image,
        output=output,
    )
    return denoise_image_execute(params, execution)


__all__ = [
    "DENOISE_IMAGE_METADATA",
    "DenoiseImageCorrectedOutputNoiseOutputs",
    "DenoiseImageCorrectedOutputNoiseParameters",
    "DenoiseImageCorrectedOutputOutputs",
    "DenoiseImageCorrectedOutputParameters",
    "DenoiseImageOutputs",
    "DenoiseImageParameters",
    "denoise_image",
    "denoise_image_corrected_output_noise_params",
    "denoise_image_corrected_output_params",
    "denoise_image_params",
]
