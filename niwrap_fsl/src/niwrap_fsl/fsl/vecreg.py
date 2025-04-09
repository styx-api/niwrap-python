# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VECREG_METADATA = Metadata(
    id="5064b1425f46565055c7ced1a7351b8b583c894d.boutiques",
    name="vecreg",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


VecregParameters = typing.TypedDict('VecregParameters', {
    "__STYX_TYPE__": typing.Literal["vecreg"],
    "input_file": InputPathType,
    "output_file": str,
    "reference_volume": InputPathType,
    "transform_file": typing.NotRequired[InputPathType | None],
    "verbose_flag": bool,
    "help_flag": bool,
    "secondary_affine": typing.NotRequired[InputPathType | None],
    "secondary_warp": typing.NotRequired[InputPathType | None],
    "interp_method": typing.NotRequired[str | None],
    "brain_mask": typing.NotRequired[InputPathType | None],
    "ref_brain_mask": typing.NotRequired[InputPathType | None],
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
        "vecreg": vecreg_cargs,
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
        "vecreg": vecreg_outputs,
    }.get(t)


class VecregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `vecreg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    registered_output: OutputPathType
    """Output file of registered vector or tensor field"""


def vecreg_params(
    input_file: InputPathType,
    output_file: str,
    reference_volume: InputPathType,
    transform_file: InputPathType | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
    secondary_affine: InputPathType | None = None,
    secondary_warp: InputPathType | None = None,
    interp_method: str | None = "trilinear",
    brain_mask: InputPathType | None = None,
    ref_brain_mask: InputPathType | None = None,
) -> VecregParameters:
    """
    Build parameters.
    
    Args:
        input_file: Filename for input vector or tensor field.
        output_file: Filename for output registered vector or tensor field.
        reference_volume: Filename for reference (target) volume.
        transform_file: Filename for affine transformation matrix.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message.
        secondary_affine: Filename for secondary affine matrix; if set, this\
            will be used for the rotation of the vector/tensor field.
        secondary_warp: Filename for secondary warp field; if set, this will be\
            used for the rotation of the vector/tensor field.
        interp_method: Interpolation method (nearestneighbour, trilinear\
            (default), sinc, or spline).
        brain_mask: Brain mask in input space.
        ref_brain_mask: Brain mask in output space (useful for speed up of\
            nonlinear registration).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "vecreg",
        "input_file": input_file,
        "output_file": output_file,
        "reference_volume": reference_volume,
        "verbose_flag": verbose_flag,
        "help_flag": help_flag,
    }
    if transform_file is not None:
        params["transform_file"] = transform_file
    if secondary_affine is not None:
        params["secondary_affine"] = secondary_affine
    if secondary_warp is not None:
        params["secondary_warp"] = secondary_warp
    if interp_method is not None:
        params["interp_method"] = interp_method
    if brain_mask is not None:
        params["brain_mask"] = brain_mask
    if ref_brain_mask is not None:
        params["ref_brain_mask"] = ref_brain_mask
    return params


def vecreg_cargs(
    params: VecregParameters,
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
    cargs.append("vecreg")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-o",
        params.get("output_file")
    ])
    cargs.extend([
        "-r",
        execution.input_file(params.get("reference_volume"))
    ])
    if params.get("transform_file") is not None:
        cargs.extend([
            "-t",
            execution.input_file(params.get("transform_file"))
        ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("help_flag"):
        cargs.append("-h")
    if params.get("secondary_affine") is not None:
        cargs.extend([
            "--rotmat",
            execution.input_file(params.get("secondary_affine"))
        ])
    if params.get("secondary_warp") is not None:
        cargs.extend([
            "--rotwarp",
            execution.input_file(params.get("secondary_warp"))
        ])
    if params.get("interp_method") is not None:
        cargs.extend([
            "--interp",
            params.get("interp_method")
        ])
    if params.get("brain_mask") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("brain_mask"))
        ])
    if params.get("ref_brain_mask") is not None:
        cargs.extend([
            "--refmask",
            execution.input_file(params.get("ref_brain_mask"))
        ])
    return cargs


def vecreg_outputs(
    params: VecregParameters,
    execution: Execution,
) -> VecregOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VecregOutputs(
        root=execution.output_file("."),
        registered_output=execution.output_file(params.get("output_file")),
    )
    return ret


def vecreg_execute(
    params: VecregParameters,
    execution: Execution,
) -> VecregOutputs:
    """
    Vector Affine/NonLinear Transformation with Orientation Preservation.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VecregOutputs`).
    """
    params = execution.params(params)
    cargs = vecreg_cargs(params, execution)
    ret = vecreg_outputs(params, execution)
    execution.run(cargs)
    return ret


def vecreg(
    input_file: InputPathType,
    output_file: str,
    reference_volume: InputPathType,
    transform_file: InputPathType | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
    secondary_affine: InputPathType | None = None,
    secondary_warp: InputPathType | None = None,
    interp_method: str | None = "trilinear",
    brain_mask: InputPathType | None = None,
    ref_brain_mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> VecregOutputs:
    """
    Vector Affine/NonLinear Transformation with Orientation Preservation.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Filename for input vector or tensor field.
        output_file: Filename for output registered vector or tensor field.
        reference_volume: Filename for reference (target) volume.
        transform_file: Filename for affine transformation matrix.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message.
        secondary_affine: Filename for secondary affine matrix; if set, this\
            will be used for the rotation of the vector/tensor field.
        secondary_warp: Filename for secondary warp field; if set, this will be\
            used for the rotation of the vector/tensor field.
        interp_method: Interpolation method (nearestneighbour, trilinear\
            (default), sinc, or spline).
        brain_mask: Brain mask in input space.
        ref_brain_mask: Brain mask in output space (useful for speed up of\
            nonlinear registration).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VecregOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VECREG_METADATA)
    params = vecreg_params(
        input_file=input_file,
        output_file=output_file,
        reference_volume=reference_volume,
        transform_file=transform_file,
        verbose_flag=verbose_flag,
        help_flag=help_flag,
        secondary_affine=secondary_affine,
        secondary_warp=secondary_warp,
        interp_method=interp_method,
        brain_mask=brain_mask,
        ref_brain_mask=ref_brain_mask,
    )
    return vecreg_execute(params, execution)


__all__ = [
    "VECREG_METADATA",
    "VecregOutputs",
    "VecregParameters",
    "vecreg",
    "vecreg_params",
]
