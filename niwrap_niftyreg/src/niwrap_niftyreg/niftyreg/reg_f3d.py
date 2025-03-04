# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

REG_F3D_METADATA = Metadata(
    id="1e4f335840b8035582d36ee0767618d0b14f496c.boutiques",
    name="reg_f3d",
    package="niftyreg",
    container_image_tag="vnmd/niftyreg_1.4.0:20220819",
)


RegF3dParameters = typing.TypedDict('RegF3dParameters', {
    "__STYX_TYPE__": typing.Literal["reg_f3d"],
    "reference_image": InputPathType,
    "floating_image": InputPathType,
    "affine_transform": typing.NotRequired[InputPathType | None],
    "flirt_affine_transform": typing.NotRequired[InputPathType | None],
    "control_point_grid_input": typing.NotRequired[InputPathType | None],
    "output_cpp": typing.NotRequired[str | None],
    "output_resampled_image": typing.NotRequired[str | None],
    "reference_mask": typing.NotRequired[InputPathType | None],
    "smooth_reference": typing.NotRequired[float | None],
    "smooth_floating": typing.NotRequired[float | None],
    "num_bins_joint_histogram": typing.NotRequired[float | None],
    "num_bins_floating_joint_histogram": typing.NotRequired[float | None],
    "lower_threshold_reference": typing.NotRequired[float | None],
    "upper_threshold_reference": typing.NotRequired[float | None],
    "lower_threshold_floating": typing.NotRequired[float | None],
    "upper_threshold_floating": typing.NotRequired[float | None],
    "spacing_x": typing.NotRequired[float | None],
    "spacing_y": typing.NotRequired[float | None],
    "spacing_z": typing.NotRequired[float | None],
    "bending_energy": typing.NotRequired[float | None],
    "linear_elasticity": typing.NotRequired[list[float] | None],
    "l2_norm_displacement": typing.NotRequired[float | None],
    "jacobian_determinant": typing.NotRequired[float | None],
    "no_approx_jl": bool,
    "no_conj": bool,
    "ssd": bool,
    "kld": bool,
    "amc": bool,
    "max_iterations": typing.NotRequired[float | None],
    "num_levels": typing.NotRequired[float | None],
    "first_levels": typing.NotRequired[float | None],
    "no_pyramid": bool,
    "symmetric": bool,
    "floating_mask": typing.NotRequired[InputPathType | None],
    "inverse_consistency": typing.NotRequired[float | None],
    "velocity_field": bool,
    "composition_steps": typing.NotRequired[float | None],
    "smooth_gradient": typing.NotRequired[float | None],
    "padding_value": typing.NotRequired[float | None],
    "verbose_off": bool,
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
        "reg_f3d": reg_f3d_cargs,
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
        "reg_f3d": reg_f3d_outputs,
    }.get(t)


class RegF3dOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_f3d(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_cpp_file: OutputPathType | None
    """File containing the output control point grid"""
    output_resampled_image_file: OutputPathType | None
    """File containing the resampled image"""


def reg_f3d_params(
    reference_image: InputPathType,
    floating_image: InputPathType,
    affine_transform: InputPathType | None = None,
    flirt_affine_transform: InputPathType | None = None,
    control_point_grid_input: InputPathType | None = None,
    output_cpp: str | None = None,
    output_resampled_image: str | None = None,
    reference_mask: InputPathType | None = None,
    smooth_reference: float | None = None,
    smooth_floating: float | None = None,
    num_bins_joint_histogram: float | None = None,
    num_bins_floating_joint_histogram: float | None = None,
    lower_threshold_reference: float | None = None,
    upper_threshold_reference: float | None = None,
    lower_threshold_floating: float | None = None,
    upper_threshold_floating: float | None = None,
    spacing_x: float | None = None,
    spacing_y: float | None = None,
    spacing_z: float | None = None,
    bending_energy: float | None = None,
    linear_elasticity: list[float] | None = None,
    l2_norm_displacement: float | None = None,
    jacobian_determinant: float | None = None,
    no_approx_jl: bool = False,
    no_conj: bool = False,
    ssd: bool = False,
    kld: bool = False,
    amc: bool = False,
    max_iterations: float | None = None,
    num_levels: float | None = None,
    first_levels: float | None = None,
    no_pyramid: bool = False,
    symmetric: bool = False,
    floating_mask: InputPathType | None = None,
    inverse_consistency: float | None = None,
    velocity_field: bool = False,
    composition_steps: float | None = None,
    smooth_gradient: float | None = None,
    padding_value: float | None = None,
    verbose_off: bool = False,
) -> RegF3dParameters:
    """
    Build parameters.
    
    Args:
        reference_image: Filename of the reference image.
        floating_image: Filename of the floating image.
        affine_transform: Filename which contains an affine transformation.
        flirt_affine_transform: Filename which contains a flirt affine\
            transformation.
        control_point_grid_input: Filename of control point grid input.
        output_cpp: Filename of control point grid.
        output_resampled_image: Filename of the resampled image.
        reference_mask: Filename of a mask image in the reference space.
        smooth_reference: Smooth the reference image using the specified sigma\
            (mm).
        smooth_floating: Smooth the floating image using the specified sigma\
            (mm).
        num_bins_joint_histogram: Number of bins to use for the joint histogram\
            (reference).
        num_bins_floating_joint_histogram: Number of bins to use for the joint\
            histogram (floating).
        lower_threshold_reference: Lower threshold to apply to the reference\
            image intensities.
        upper_threshold_reference: Upper threshold to apply to the reference\
            image intensities.
        lower_threshold_floating: Lower threshold to apply to the floating\
            image intensities.
        upper_threshold_floating: Upper threshold to apply to the floating\
            image intensities.
        spacing_x: Final grid spacing along the x axis in mm (or in voxel if\
            negative value).
        spacing_y: Final grid spacing along the y axis in mm (or in voxel if\
            negative value).
        spacing_z: Final grid spacing along the z axis in mm (or in voxel if\
            negative value).
        bending_energy: Weight of the bending energy penalty term.
        linear_elasticity: Weights of linear elasticity penalty term.
        l2_norm_displacement: Weight of L2 norm displacement penalty term.
        jacobian_determinant: Weight of log of the Jacobian determinant penalty\
            term.
        no_approx_jl: Do not approximate the JL value only at the control point\
            position.
        no_conj: Do not use the conjugate gradient optimization but a simple\
            gradient ascent.
        ssd: Use the SSD as the similarity measure instead of NMI.
        kld: Use the KL divergence as the similarity measure instead of NMI.
        amc: Use the additive NMI for multichannel data.
        max_iterations: Maximal number of iterations per level.
        num_levels: Number of levels to perform.
        first_levels: Only perform the first levels.
        no_pyramid: Do not use a pyramidal approach.
        symmetric: Use symmetric approach.
        floating_mask: Filename of a mask image in the floating space.
        inverse_consistency: Weight of the inverse consistency penalty term.
        velocity_field: Use velocity field integration to generate the\
            deformation.
        composition_steps: Number of composition steps.
        smooth_gradient: Smooth the metric derivative (in mm).
        padding_value: Padding value.
        verbose_off: Turn verbose off.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "reg_f3d",
        "reference_image": reference_image,
        "floating_image": floating_image,
        "no_approx_jl": no_approx_jl,
        "no_conj": no_conj,
        "ssd": ssd,
        "kld": kld,
        "amc": amc,
        "no_pyramid": no_pyramid,
        "symmetric": symmetric,
        "velocity_field": velocity_field,
        "verbose_off": verbose_off,
    }
    if affine_transform is not None:
        params["affine_transform"] = affine_transform
    if flirt_affine_transform is not None:
        params["flirt_affine_transform"] = flirt_affine_transform
    if control_point_grid_input is not None:
        params["control_point_grid_input"] = control_point_grid_input
    if output_cpp is not None:
        params["output_cpp"] = output_cpp
    if output_resampled_image is not None:
        params["output_resampled_image"] = output_resampled_image
    if reference_mask is not None:
        params["reference_mask"] = reference_mask
    if smooth_reference is not None:
        params["smooth_reference"] = smooth_reference
    if smooth_floating is not None:
        params["smooth_floating"] = smooth_floating
    if num_bins_joint_histogram is not None:
        params["num_bins_joint_histogram"] = num_bins_joint_histogram
    if num_bins_floating_joint_histogram is not None:
        params["num_bins_floating_joint_histogram"] = num_bins_floating_joint_histogram
    if lower_threshold_reference is not None:
        params["lower_threshold_reference"] = lower_threshold_reference
    if upper_threshold_reference is not None:
        params["upper_threshold_reference"] = upper_threshold_reference
    if lower_threshold_floating is not None:
        params["lower_threshold_floating"] = lower_threshold_floating
    if upper_threshold_floating is not None:
        params["upper_threshold_floating"] = upper_threshold_floating
    if spacing_x is not None:
        params["spacing_x"] = spacing_x
    if spacing_y is not None:
        params["spacing_y"] = spacing_y
    if spacing_z is not None:
        params["spacing_z"] = spacing_z
    if bending_energy is not None:
        params["bending_energy"] = bending_energy
    if linear_elasticity is not None:
        params["linear_elasticity"] = linear_elasticity
    if l2_norm_displacement is not None:
        params["l2_norm_displacement"] = l2_norm_displacement
    if jacobian_determinant is not None:
        params["jacobian_determinant"] = jacobian_determinant
    if max_iterations is not None:
        params["max_iterations"] = max_iterations
    if num_levels is not None:
        params["num_levels"] = num_levels
    if first_levels is not None:
        params["first_levels"] = first_levels
    if floating_mask is not None:
        params["floating_mask"] = floating_mask
    if inverse_consistency is not None:
        params["inverse_consistency"] = inverse_consistency
    if composition_steps is not None:
        params["composition_steps"] = composition_steps
    if smooth_gradient is not None:
        params["smooth_gradient"] = smooth_gradient
    if padding_value is not None:
        params["padding_value"] = padding_value
    return params


def reg_f3d_cargs(
    params: RegF3dParameters,
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
    cargs.append("reg_f3d")
    cargs.extend([
        "-ref",
        execution.input_file(params.get("reference_image"))
    ])
    cargs.extend([
        "-flo",
        execution.input_file(params.get("floating_image"))
    ])
    if params.get("affine_transform") is not None:
        cargs.extend([
            "-aff",
            execution.input_file(params.get("affine_transform"))
        ])
    if params.get("flirt_affine_transform") is not None:
        cargs.extend([
            "-affFlirt",
            execution.input_file(params.get("flirt_affine_transform"))
        ])
    if params.get("control_point_grid_input") is not None:
        cargs.extend([
            "-incpp",
            execution.input_file(params.get("control_point_grid_input"))
        ])
    if params.get("output_cpp") is not None:
        cargs.extend([
            "-cpp",
            params.get("output_cpp")
        ])
    if params.get("output_resampled_image") is not None:
        cargs.extend([
            "-res",
            params.get("output_resampled_image")
        ])
    if params.get("reference_mask") is not None:
        cargs.extend([
            "-rmask",
            execution.input_file(params.get("reference_mask"))
        ])
    if params.get("smooth_reference") is not None:
        cargs.extend([
            "-smooR",
            str(params.get("smooth_reference"))
        ])
    if params.get("smooth_floating") is not None:
        cargs.extend([
            "-smooF",
            str(params.get("smooth_floating"))
        ])
    if params.get("num_bins_joint_histogram") is not None:
        cargs.extend([
            "--rbn",
            str(params.get("num_bins_joint_histogram"))
        ])
    if params.get("num_bins_floating_joint_histogram") is not None:
        cargs.extend([
            "--fbn",
            str(params.get("num_bins_floating_joint_histogram"))
        ])
    if params.get("lower_threshold_reference") is not None:
        cargs.extend([
            "--rLwTh",
            str(params.get("lower_threshold_reference"))
        ])
    if params.get("upper_threshold_reference") is not None:
        cargs.extend([
            "--rUpTh",
            str(params.get("upper_threshold_reference"))
        ])
    if params.get("lower_threshold_floating") is not None:
        cargs.extend([
            "--fLwTh",
            str(params.get("lower_threshold_floating"))
        ])
    if params.get("upper_threshold_floating") is not None:
        cargs.extend([
            "--fUpTh",
            str(params.get("upper_threshold_floating"))
        ])
    if params.get("spacing_x") is not None:
        cargs.extend([
            "-sx",
            str(params.get("spacing_x"))
        ])
    if params.get("spacing_y") is not None:
        cargs.extend([
            "-sy",
            str(params.get("spacing_y"))
        ])
    if params.get("spacing_z") is not None:
        cargs.extend([
            "-sz",
            str(params.get("spacing_z"))
        ])
    if params.get("bending_energy") is not None:
        cargs.extend([
            "-be",
            str(params.get("bending_energy"))
        ])
    if params.get("linear_elasticity") is not None:
        cargs.extend([
            "-le",
            *map(str, params.get("linear_elasticity"))
        ])
    if params.get("l2_norm_displacement") is not None:
        cargs.extend([
            "-l2",
            str(params.get("l2_norm_displacement"))
        ])
    if params.get("jacobian_determinant") is not None:
        cargs.extend([
            "-jl",
            str(params.get("jacobian_determinant"))
        ])
    if params.get("no_approx_jl"):
        cargs.append("-noAppJL")
    if params.get("no_conj"):
        cargs.append("-noConj")
    if params.get("ssd"):
        cargs.append("-ssd")
    if params.get("kld"):
        cargs.append("-kld")
    if params.get("amc"):
        cargs.append("-amc")
    if params.get("max_iterations") is not None:
        cargs.extend([
            "-maxit",
            str(params.get("max_iterations"))
        ])
    if params.get("num_levels") is not None:
        cargs.extend([
            "-ln",
            str(params.get("num_levels"))
        ])
    if params.get("first_levels") is not None:
        cargs.extend([
            "-lp",
            str(params.get("first_levels"))
        ])
    if params.get("no_pyramid"):
        cargs.append("-nopy")
    if params.get("symmetric"):
        cargs.append("-sym")
    if params.get("floating_mask") is not None:
        cargs.extend([
            "-fmask",
            execution.input_file(params.get("floating_mask"))
        ])
    if params.get("inverse_consistency") is not None:
        cargs.extend([
            "-ic",
            str(params.get("inverse_consistency"))
        ])
    if params.get("velocity_field"):
        cargs.append("-vel")
    if params.get("composition_steps") is not None:
        cargs.extend([
            "-step",
            str(params.get("composition_steps"))
        ])
    if params.get("smooth_gradient") is not None:
        cargs.extend([
            "-smoothGrad",
            str(params.get("smooth_gradient"))
        ])
    if params.get("padding_value") is not None:
        cargs.extend([
            "-pad",
            str(params.get("padding_value"))
        ])
    if params.get("verbose_off"):
        cargs.append("-voff")
    return cargs


def reg_f3d_outputs(
    params: RegF3dParameters,
    execution: Execution,
) -> RegF3dOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RegF3dOutputs(
        root=execution.output_file("."),
        output_cpp_file=execution.output_file(params.get("output_cpp")) if (params.get("output_cpp") is not None) else None,
        output_resampled_image_file=execution.output_file(params.get("output_resampled_image")) if (params.get("output_resampled_image") is not None) else None,
    )
    return ret


def reg_f3d_execute(
    params: RegF3dParameters,
    execution: Execution,
) -> RegF3dOutputs:
    """
    Fast Free-Form Deformation algorithm for non-rigid registration based on
    Rueckert's 99 TMI work.
    
    Author: NiftyReg Developers
    
    URL: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RegF3dOutputs`).
    """
    params = execution.params(params)
    cargs = reg_f3d_cargs(params, execution)
    ret = reg_f3d_outputs(params, execution)
    execution.run(cargs)
    return ret


def reg_f3d(
    reference_image: InputPathType,
    floating_image: InputPathType,
    affine_transform: InputPathType | None = None,
    flirt_affine_transform: InputPathType | None = None,
    control_point_grid_input: InputPathType | None = None,
    output_cpp: str | None = None,
    output_resampled_image: str | None = None,
    reference_mask: InputPathType | None = None,
    smooth_reference: float | None = None,
    smooth_floating: float | None = None,
    num_bins_joint_histogram: float | None = None,
    num_bins_floating_joint_histogram: float | None = None,
    lower_threshold_reference: float | None = None,
    upper_threshold_reference: float | None = None,
    lower_threshold_floating: float | None = None,
    upper_threshold_floating: float | None = None,
    spacing_x: float | None = None,
    spacing_y: float | None = None,
    spacing_z: float | None = None,
    bending_energy: float | None = None,
    linear_elasticity: list[float] | None = None,
    l2_norm_displacement: float | None = None,
    jacobian_determinant: float | None = None,
    no_approx_jl: bool = False,
    no_conj: bool = False,
    ssd: bool = False,
    kld: bool = False,
    amc: bool = False,
    max_iterations: float | None = None,
    num_levels: float | None = None,
    first_levels: float | None = None,
    no_pyramid: bool = False,
    symmetric: bool = False,
    floating_mask: InputPathType | None = None,
    inverse_consistency: float | None = None,
    velocity_field: bool = False,
    composition_steps: float | None = None,
    smooth_gradient: float | None = None,
    padding_value: float | None = None,
    verbose_off: bool = False,
    runner: Runner | None = None,
) -> RegF3dOutputs:
    """
    Fast Free-Form Deformation algorithm for non-rigid registration based on
    Rueckert's 99 TMI work.
    
    Author: NiftyReg Developers
    
    URL: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        reference_image: Filename of the reference image.
        floating_image: Filename of the floating image.
        affine_transform: Filename which contains an affine transformation.
        flirt_affine_transform: Filename which contains a flirt affine\
            transformation.
        control_point_grid_input: Filename of control point grid input.
        output_cpp: Filename of control point grid.
        output_resampled_image: Filename of the resampled image.
        reference_mask: Filename of a mask image in the reference space.
        smooth_reference: Smooth the reference image using the specified sigma\
            (mm).
        smooth_floating: Smooth the floating image using the specified sigma\
            (mm).
        num_bins_joint_histogram: Number of bins to use for the joint histogram\
            (reference).
        num_bins_floating_joint_histogram: Number of bins to use for the joint\
            histogram (floating).
        lower_threshold_reference: Lower threshold to apply to the reference\
            image intensities.
        upper_threshold_reference: Upper threshold to apply to the reference\
            image intensities.
        lower_threshold_floating: Lower threshold to apply to the floating\
            image intensities.
        upper_threshold_floating: Upper threshold to apply to the floating\
            image intensities.
        spacing_x: Final grid spacing along the x axis in mm (or in voxel if\
            negative value).
        spacing_y: Final grid spacing along the y axis in mm (or in voxel if\
            negative value).
        spacing_z: Final grid spacing along the z axis in mm (or in voxel if\
            negative value).
        bending_energy: Weight of the bending energy penalty term.
        linear_elasticity: Weights of linear elasticity penalty term.
        l2_norm_displacement: Weight of L2 norm displacement penalty term.
        jacobian_determinant: Weight of log of the Jacobian determinant penalty\
            term.
        no_approx_jl: Do not approximate the JL value only at the control point\
            position.
        no_conj: Do not use the conjugate gradient optimization but a simple\
            gradient ascent.
        ssd: Use the SSD as the similarity measure instead of NMI.
        kld: Use the KL divergence as the similarity measure instead of NMI.
        amc: Use the additive NMI for multichannel data.
        max_iterations: Maximal number of iterations per level.
        num_levels: Number of levels to perform.
        first_levels: Only perform the first levels.
        no_pyramid: Do not use a pyramidal approach.
        symmetric: Use symmetric approach.
        floating_mask: Filename of a mask image in the floating space.
        inverse_consistency: Weight of the inverse consistency penalty term.
        velocity_field: Use velocity field integration to generate the\
            deformation.
        composition_steps: Number of composition steps.
        smooth_gradient: Smooth the metric derivative (in mm).
        padding_value: Padding value.
        verbose_off: Turn verbose off.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegF3dOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_F3D_METADATA)
    params = reg_f3d_params(
        reference_image=reference_image,
        floating_image=floating_image,
        affine_transform=affine_transform,
        flirt_affine_transform=flirt_affine_transform,
        control_point_grid_input=control_point_grid_input,
        output_cpp=output_cpp,
        output_resampled_image=output_resampled_image,
        reference_mask=reference_mask,
        smooth_reference=smooth_reference,
        smooth_floating=smooth_floating,
        num_bins_joint_histogram=num_bins_joint_histogram,
        num_bins_floating_joint_histogram=num_bins_floating_joint_histogram,
        lower_threshold_reference=lower_threshold_reference,
        upper_threshold_reference=upper_threshold_reference,
        lower_threshold_floating=lower_threshold_floating,
        upper_threshold_floating=upper_threshold_floating,
        spacing_x=spacing_x,
        spacing_y=spacing_y,
        spacing_z=spacing_z,
        bending_energy=bending_energy,
        linear_elasticity=linear_elasticity,
        l2_norm_displacement=l2_norm_displacement,
        jacobian_determinant=jacobian_determinant,
        no_approx_jl=no_approx_jl,
        no_conj=no_conj,
        ssd=ssd,
        kld=kld,
        amc=amc,
        max_iterations=max_iterations,
        num_levels=num_levels,
        first_levels=first_levels,
        no_pyramid=no_pyramid,
        symmetric=symmetric,
        floating_mask=floating_mask,
        inverse_consistency=inverse_consistency,
        velocity_field=velocity_field,
        composition_steps=composition_steps,
        smooth_gradient=smooth_gradient,
        padding_value=padding_value,
        verbose_off=verbose_off,
    )
    return reg_f3d_execute(params, execution)


__all__ = [
    "REG_F3D_METADATA",
    "RegF3dOutputs",
    "RegF3dParameters",
    "reg_f3d",
    "reg_f3d_params",
]
