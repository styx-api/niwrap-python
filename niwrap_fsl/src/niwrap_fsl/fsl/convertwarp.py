# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CONVERTWARP_METADATA = Metadata(
    id="abbc9808b6350a6d6a267687556e5ef284b82f97.boutiques",
    name="convertwarp",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


ConvertwarpParameters = typing.TypedDict('ConvertwarpParameters', {
    "__STYX_TYPE__": typing.Literal["convertwarp"],
    "abswarp": bool,
    "cons_jacobian": bool,
    "jacobian_max": typing.NotRequired[float | None],
    "jacobian_min": typing.NotRequired[float | None],
    "midmat": typing.NotRequired[InputPathType | None],
    "out_abswarp": bool,
    "out_relwarp": bool,
    "output_type": typing.NotRequired[typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None],
    "postmat": typing.NotRequired[InputPathType | None],
    "premat": typing.NotRequired[InputPathType | None],
    "reference": InputPathType,
    "relwarp": bool,
    "shift_direction": typing.NotRequired[typing.Literal["y-", "y", "x", "x-", "z", "z-"] | None],
    "shift_in_file": typing.NotRequired[InputPathType | None],
    "warp1": typing.NotRequired[InputPathType | None],
    "warp2": typing.NotRequired[InputPathType | None],
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
        "convertwarp": convertwarp_cargs,
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
        "convertwarp": convertwarp_outputs,
    }.get(t)


class ConvertwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convertwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Name of output file, containing warps that are the combination of all
    those given as arguments. the format of this will be a field-file (rather
    than spline coefficients) with any affine components included."""
    out_file_: OutputPathType
    """Name of output file, containing the warp as field or coefficients."""


def convertwarp_params(
    reference: InputPathType,
    abswarp: bool = False,
    cons_jacobian: bool = False,
    jacobian_max: float | None = None,
    jacobian_min: float | None = None,
    midmat: InputPathType | None = None,
    out_abswarp: bool = False,
    out_relwarp: bool = False,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    postmat: InputPathType | None = None,
    premat: InputPathType | None = None,
    relwarp: bool = False,
    shift_direction: typing.Literal["y-", "y", "x", "x-", "z", "z-"] | None = None,
    shift_in_file: InputPathType | None = None,
    warp1: InputPathType | None = None,
    warp2: InputPathType | None = None,
) -> ConvertwarpParameters:
    """
    Build parameters.
    
    Args:
        reference: Name of a file in target space of the full transform.
        abswarp: If set it indicates that the warps in --warp1 and --warp2\
            should be interpreted as absolute. i.e. the values in --warp1/2 are the\
            coordinates in the next space, rather than displacements. this flag is\
            ignored if --warp1/2 was created by fnirt, which always creates\
            relative displacements.
        cons_jacobian: Constrain the jacobian of the warpfield to lie within\
            specified min/max limits.
        jacobian_max: Maximum acceptable jacobian value for constraint (default\
            100.0).
        jacobian_min: Minimum acceptable jacobian value for constraint (default\
            0.01).
        midmat: Name of file containing mid-warp-affine transform.
        out_abswarp: If set it indicates that the warps in --out should be\
            absolute, i.e. the values in --out are displacements from the\
            coordinates in --ref.
        out_relwarp: If set it indicates that the warps in --out should be\
            relative, i.e. the values in --out are displacements from the\
            coordinates in --ref.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        postmat: Name of file containing an affine transform (applied last). it\
            could e.g. be an affine transform that maps the mni152-space into a\
            better approximation to the talairach-space (if indeed there is one).
        premat: Filename for pre-transform (affine matrix).
        relwarp: If set it indicates that the warps in --warp1/2 should be\
            interpreted as relative. i.e. the values in --warp1/2 are displacements\
            from the coordinates in the next space.
        shift_direction: 'y-' or 'y' or 'x' or 'x-' or 'z' or 'z-'. Indicates\
            the direction that the distortions from --shiftmap goes. it depends on\
            the direction and polarity of the phase-encoding in the epi sequence.
        shift_in_file: Name of file containing a "shiftmap", a non-linear\
            transform with displacements only in one direction (applied first,\
            before premat). this would typically be a fieldmap that has been\
            pre-processed using fugue that maps a subjects functional (epi) data\
            onto an undistorted space (i.e. a space that corresponds to his/her\
            true anatomy).
        warp1: Name of file containing initial warp-fields/coefficients\
            (follows premat). this could e.g. be a fnirt-transform from a subjects\
            structural scan to an average of a group of subjects.
        warp2: Name of file containing secondary warp-fields/coefficients\
            (after warp1/midmat but before postmat). this could e.g. be a\
            fnirt-transform from the average of a group of subjects to some\
            standard space (e.g. mni152).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "convertwarp",
        "abswarp": abswarp,
        "cons_jacobian": cons_jacobian,
        "out_abswarp": out_abswarp,
        "out_relwarp": out_relwarp,
        "reference": reference,
        "relwarp": relwarp,
    }
    if jacobian_max is not None:
        params["jacobian_max"] = jacobian_max
    if jacobian_min is not None:
        params["jacobian_min"] = jacobian_min
    if midmat is not None:
        params["midmat"] = midmat
    if output_type is not None:
        params["output_type"] = output_type
    if postmat is not None:
        params["postmat"] = postmat
    if premat is not None:
        params["premat"] = premat
    if shift_direction is not None:
        params["shift_direction"] = shift_direction
    if shift_in_file is not None:
        params["shift_in_file"] = shift_in_file
    if warp1 is not None:
        params["warp1"] = warp1
    if warp2 is not None:
        params["warp2"] = warp2
    return params


def convertwarp_cargs(
    params: ConvertwarpParameters,
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
    cargs.append("convertwarp")
    if params.get("abswarp"):
        cargs.append("--abs")
    if params.get("cons_jacobian"):
        cargs.append("--constrainj")
    if params.get("jacobian_max") is not None:
        cargs.append("--jmax=" + str(params.get("jacobian_max")))
    if params.get("jacobian_min") is not None:
        cargs.append("--jmin=" + str(params.get("jacobian_min")))
    if params.get("midmat") is not None:
        cargs.append("--midmat=" + execution.input_file(params.get("midmat")))
    if params.get("out_abswarp"):
        cargs.append("--absout")
    if params.get("out_relwarp"):
        cargs.append("--relout")
    if params.get("output_type") is not None:
        cargs.append(params.get("output_type"))
    if params.get("postmat") is not None:
        cargs.append("--postmat=" + execution.input_file(params.get("postmat")))
    if params.get("premat") is not None:
        cargs.append("--premat=" + execution.input_file(params.get("premat")))
    cargs.append("--ref=" + execution.input_file(params.get("reference")))
    if params.get("relwarp"):
        cargs.append("--rel")
    if params.get("shift_direction") is not None:
        cargs.append("--shiftdir=" + params.get("shift_direction"))
    if params.get("shift_in_file") is not None:
        cargs.append("--shiftmap=" + execution.input_file(params.get("shift_in_file")))
    if params.get("warp1") is not None:
        cargs.append("--warp1=" + execution.input_file(params.get("warp1")))
    if params.get("warp2") is not None:
        cargs.append("--warp2=" + execution.input_file(params.get("warp2")))
    return cargs


def convertwarp_outputs(
    params: ConvertwarpParameters,
    execution: Execution,
) -> ConvertwarpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ConvertwarpOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(params.get("reference")).name + "_concatwarp"),
        out_file_=execution.output_file("out_file"),
    )
    return ret


def convertwarp_execute(
    params: ConvertwarpParameters,
    execution: Execution,
) -> ConvertwarpOutputs:
    """
    Use FSL convertwarp for combining multiple transforms into one.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ConvertwarpOutputs`).
    """
    params = execution.params(params)
    cargs = convertwarp_cargs(params, execution)
    ret = convertwarp_outputs(params, execution)
    execution.run(cargs)
    return ret


def convertwarp(
    reference: InputPathType,
    abswarp: bool = False,
    cons_jacobian: bool = False,
    jacobian_max: float | None = None,
    jacobian_min: float | None = None,
    midmat: InputPathType | None = None,
    out_abswarp: bool = False,
    out_relwarp: bool = False,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    postmat: InputPathType | None = None,
    premat: InputPathType | None = None,
    relwarp: bool = False,
    shift_direction: typing.Literal["y-", "y", "x", "x-", "z", "z-"] | None = None,
    shift_in_file: InputPathType | None = None,
    warp1: InputPathType | None = None,
    warp2: InputPathType | None = None,
    runner: Runner | None = None,
) -> ConvertwarpOutputs:
    """
    Use FSL convertwarp for combining multiple transforms into one.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        reference: Name of a file in target space of the full transform.
        abswarp: If set it indicates that the warps in --warp1 and --warp2\
            should be interpreted as absolute. i.e. the values in --warp1/2 are the\
            coordinates in the next space, rather than displacements. this flag is\
            ignored if --warp1/2 was created by fnirt, which always creates\
            relative displacements.
        cons_jacobian: Constrain the jacobian of the warpfield to lie within\
            specified min/max limits.
        jacobian_max: Maximum acceptable jacobian value for constraint (default\
            100.0).
        jacobian_min: Minimum acceptable jacobian value for constraint (default\
            0.01).
        midmat: Name of file containing mid-warp-affine transform.
        out_abswarp: If set it indicates that the warps in --out should be\
            absolute, i.e. the values in --out are displacements from the\
            coordinates in --ref.
        out_relwarp: If set it indicates that the warps in --out should be\
            relative, i.e. the values in --out are displacements from the\
            coordinates in --ref.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        postmat: Name of file containing an affine transform (applied last). it\
            could e.g. be an affine transform that maps the mni152-space into a\
            better approximation to the talairach-space (if indeed there is one).
        premat: Filename for pre-transform (affine matrix).
        relwarp: If set it indicates that the warps in --warp1/2 should be\
            interpreted as relative. i.e. the values in --warp1/2 are displacements\
            from the coordinates in the next space.
        shift_direction: 'y-' or 'y' or 'x' or 'x-' or 'z' or 'z-'. Indicates\
            the direction that the distortions from --shiftmap goes. it depends on\
            the direction and polarity of the phase-encoding in the epi sequence.
        shift_in_file: Name of file containing a "shiftmap", a non-linear\
            transform with displacements only in one direction (applied first,\
            before premat). this would typically be a fieldmap that has been\
            pre-processed using fugue that maps a subjects functional (epi) data\
            onto an undistorted space (i.e. a space that corresponds to his/her\
            true anatomy).
        warp1: Name of file containing initial warp-fields/coefficients\
            (follows premat). this could e.g. be a fnirt-transform from a subjects\
            structural scan to an average of a group of subjects.
        warp2: Name of file containing secondary warp-fields/coefficients\
            (after warp1/midmat but before postmat). this could e.g. be a\
            fnirt-transform from the average of a group of subjects to some\
            standard space (e.g. mni152).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERTWARP_METADATA)
    params = convertwarp_params(
        abswarp=abswarp,
        cons_jacobian=cons_jacobian,
        jacobian_max=jacobian_max,
        jacobian_min=jacobian_min,
        midmat=midmat,
        out_abswarp=out_abswarp,
        out_relwarp=out_relwarp,
        output_type=output_type,
        postmat=postmat,
        premat=premat,
        reference=reference,
        relwarp=relwarp,
        shift_direction=shift_direction,
        shift_in_file=shift_in_file,
        warp1=warp1,
        warp2=warp2,
    )
    return convertwarp_execute(params, execution)


__all__ = [
    "CONVERTWARP_METADATA",
    "ConvertwarpOutputs",
    "ConvertwarpParameters",
    "convertwarp",
    "convertwarp_params",
]
