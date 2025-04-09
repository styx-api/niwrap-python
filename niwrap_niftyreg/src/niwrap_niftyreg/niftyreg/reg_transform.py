# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

REG_TRANSFORM_METADATA = Metadata(
    id="526dd4229bf4ca8feec0463e36f47c648924cbae.boutiques",
    name="reg_transform",
    package="niftyreg",
    container_image_tag="vnmd/niftyreg_1.4.0:20220819",
)


RegTransformParameters = typing.TypedDict('RegTransformParameters', {
    "__STYX_TYPE__": typing.Literal["reg_transform"],
    "reference_image": InputPathType,
    "cpp2def_input": typing.NotRequired[InputPathType | None],
    "cpp2def_output": typing.NotRequired[str | None],
    "comp1_cpp2": typing.NotRequired[InputPathType | None],
    "comp1_cpp1": typing.NotRequired[InputPathType | None],
    "comp1_output": typing.NotRequired[str | None],
    "comp2_cpp": typing.NotRequired[InputPathType | None],
    "comp2_def": typing.NotRequired[InputPathType | None],
    "comp2_output": typing.NotRequired[str | None],
    "comp3_def2": typing.NotRequired[InputPathType | None],
    "comp3_def1": typing.NotRequired[InputPathType | None],
    "comp3_output": typing.NotRequired[str | None],
    "def2disp_input": typing.NotRequired[InputPathType | None],
    "def2disp_output": typing.NotRequired[str | None],
    "disp2def_input": typing.NotRequired[InputPathType | None],
    "disp2def_output": typing.NotRequired[str | None],
    "upd_sform_image": typing.NotRequired[InputPathType | None],
    "upd_sform_affine": typing.NotRequired[InputPathType | None],
    "upd_sform_output": typing.NotRequired[str | None],
    "aff2def_affine": typing.NotRequired[InputPathType | None],
    "aff2def_target": typing.NotRequired[InputPathType | None],
    "aff2def_cpp_or_def": typing.NotRequired[InputPathType | None],
    "aff2def_output": typing.NotRequired[str | None],
    "inv_affine_input": typing.NotRequired[InputPathType | None],
    "inv_affine_output": typing.NotRequired[str | None],
    "comp_aff_1st": typing.NotRequired[InputPathType | None],
    "comp_aff_2nd": typing.NotRequired[InputPathType | None],
    "comp_aff_output": typing.NotRequired[str | None],
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
        "reg_transform": reg_transform_cargs,
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
        "reg_transform": reg_transform_outputs,
    }.get(t)


class RegTransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_transform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cpp2def_output_file: OutputPathType | None
    """File containing the CPP to DEF converted deformation field."""
    comp1_output_file: OutputPathType | None
    """File containing the composed deformation field from two control point
    lattices."""
    comp2_output_file: OutputPathType | None
    """File containing the composed deformation field from a deformation field
    and a control point lattice."""
    comp3_output_file: OutputPathType | None
    """File containing the composed deformation field from two deformation
    fields."""
    def2disp_output_file: OutputPathType | None
    """File containing the converted displacement field from a deformation
    field."""
    disp2def_output_file: OutputPathType | None
    """File containing the converted deformation field from a displacement
    field."""
    upd_sform_output_file: OutputPathType | None
    """File containing the updated image with modified sform."""
    aff2def_output_file: OutputPathType | None
    """File containing the composed deformation field from a non-rigid and an
    affine transformation."""
    inv_affine_output_file: OutputPathType | None
    """File containing the inverted affine matrix."""
    comp_aff_output_file: OutputPathType | None
    """File containing the composed affine matrix."""


def reg_transform_params(
    reference_image: InputPathType,
    cpp2def_input: InputPathType | None = None,
    cpp2def_output: str | None = None,
    comp1_cpp2: InputPathType | None = None,
    comp1_cpp1: InputPathType | None = None,
    comp1_output: str | None = None,
    comp2_cpp: InputPathType | None = None,
    comp2_def: InputPathType | None = None,
    comp2_output: str | None = None,
    comp3_def2: InputPathType | None = None,
    comp3_def1: InputPathType | None = None,
    comp3_output: str | None = None,
    def2disp_input: InputPathType | None = None,
    def2disp_output: str | None = None,
    disp2def_input: InputPathType | None = None,
    disp2def_output: str | None = None,
    upd_sform_image: InputPathType | None = None,
    upd_sform_affine: InputPathType | None = None,
    upd_sform_output: str | None = None,
    aff2def_affine: InputPathType | None = None,
    aff2def_target: InputPathType | None = None,
    aff2def_cpp_or_def: InputPathType | None = None,
    aff2def_output: str | None = None,
    inv_affine_input: InputPathType | None = None,
    inv_affine_output: str | None = None,
    comp_aff_1st: InputPathType | None = None,
    comp_aff_2nd: InputPathType | None = None,
    comp_aff_output: str | None = None,
) -> RegTransformParameters:
    """
    Build parameters.
    
    Args:
        reference_image: Filename of the reference image.
        cpp2def_input: Conversion from control point position to deformation\
            field. Filename of input lattice of control point positions (CPP).
        cpp2def_output: Filename of the output deformation field image (DEF).
        comp1_cpp2: Composition of two lattices of control points.\
            CPP2(CPP1(x)). Filename of lattice of control point that contains the\
            second deformation (CPP2).
        comp1_cpp1: Filename of lattice of control point that contains the\
            initial deformation (CPP1).
        comp1_output: Filename of the output deformation field.
        comp2_cpp: Composition of a deformation field with a lattice of control\
            points. CPP(DEF(x)). Filename of lattice of control point that contains\
            the second deformation (CPP).
        comp2_def: Filename of the deformation field to be used as initial\
            deformation (DEF).
        comp2_output: Filename of the output deformation field.
        comp3_def2: Composition of two deformation fields. DEF2(DEF1(x)).\
            Filename of the second deformation field (DEF2).
        comp3_def1: Filename of the first deformation field (DEF1).
        comp3_output: Filename of the output deformation field.
        def2disp_input: Convert a deformation field into a displacement field.\
            Filename of deformation field x'=T(x).
        def2disp_output: Filename of displacement field x'=x+T(x).
        disp2def_input: Convert a displacement field into a deformation field.\
            Filename of displacement field x'=x+T(x).
        disp2def_output: Filename of deformation field x'=T(x).
        upd_sform_image: Update the sform of a floating (source) image using an\
            affine transformation. Filename of image to be updated.
        upd_sform_affine: Affine transformation defined as Affine x Reference =\
            Floating. Filename of affine transformation.
        upd_sform_output: Updated image filename.
        aff2def_affine: Compose a non-rigid with an affine. Filename of affine\
            transformation.
        aff2def_target: Image used as a target for the non-rigid step.
        aff2def_cpp_or_def: Reference image (B). Filename of control point\
            position or deformation field.
        aff2def_output: Output deformation field filename.
        inv_affine_input: Invert an affine transformation matrix. Filename of\
            input affine matrix.
        inv_affine_output: Filename of inverted affine matrix.
        comp_aff_1st: Compose two affine transformation matrices. Filename of\
            first affine matrix.
        comp_aff_2nd: Filename of second affine matrix.
        comp_aff_output: Filename of composed affine matrix result.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "reg_transform",
        "reference_image": reference_image,
    }
    if cpp2def_input is not None:
        params["cpp2def_input"] = cpp2def_input
    if cpp2def_output is not None:
        params["cpp2def_output"] = cpp2def_output
    if comp1_cpp2 is not None:
        params["comp1_cpp2"] = comp1_cpp2
    if comp1_cpp1 is not None:
        params["comp1_cpp1"] = comp1_cpp1
    if comp1_output is not None:
        params["comp1_output"] = comp1_output
    if comp2_cpp is not None:
        params["comp2_cpp"] = comp2_cpp
    if comp2_def is not None:
        params["comp2_def"] = comp2_def
    if comp2_output is not None:
        params["comp2_output"] = comp2_output
    if comp3_def2 is not None:
        params["comp3_def2"] = comp3_def2
    if comp3_def1 is not None:
        params["comp3_def1"] = comp3_def1
    if comp3_output is not None:
        params["comp3_output"] = comp3_output
    if def2disp_input is not None:
        params["def2disp_input"] = def2disp_input
    if def2disp_output is not None:
        params["def2disp_output"] = def2disp_output
    if disp2def_input is not None:
        params["disp2def_input"] = disp2def_input
    if disp2def_output is not None:
        params["disp2def_output"] = disp2def_output
    if upd_sform_image is not None:
        params["upd_sform_image"] = upd_sform_image
    if upd_sform_affine is not None:
        params["upd_sform_affine"] = upd_sform_affine
    if upd_sform_output is not None:
        params["upd_sform_output"] = upd_sform_output
    if aff2def_affine is not None:
        params["aff2def_affine"] = aff2def_affine
    if aff2def_target is not None:
        params["aff2def_target"] = aff2def_target
    if aff2def_cpp_or_def is not None:
        params["aff2def_cpp_or_def"] = aff2def_cpp_or_def
    if aff2def_output is not None:
        params["aff2def_output"] = aff2def_output
    if inv_affine_input is not None:
        params["inv_affine_input"] = inv_affine_input
    if inv_affine_output is not None:
        params["inv_affine_output"] = inv_affine_output
    if comp_aff_1st is not None:
        params["comp_aff_1st"] = comp_aff_1st
    if comp_aff_2nd is not None:
        params["comp_aff_2nd"] = comp_aff_2nd
    if comp_aff_output is not None:
        params["comp_aff_output"] = comp_aff_output
    return params


def reg_transform_cargs(
    params: RegTransformParameters,
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
    cargs.append("reg_transform")
    cargs.extend([
        "-ref",
        execution.input_file(params.get("reference_image"))
    ])
    if params.get("cpp2def_input") is not None:
        cargs.extend([
            "-cpp2def",
            execution.input_file(params.get("cpp2def_input"))
        ])
    if params.get("cpp2def_output") is not None:
        cargs.append(params.get("cpp2def_output"))
    if params.get("comp1_cpp2") is not None:
        cargs.extend([
            "-comp1",
            execution.input_file(params.get("comp1_cpp2"))
        ])
    if params.get("comp1_cpp1") is not None:
        cargs.append(execution.input_file(params.get("comp1_cpp1")))
    if params.get("comp1_output") is not None:
        cargs.append(params.get("comp1_output"))
    if params.get("comp2_cpp") is not None:
        cargs.extend([
            "-comp2",
            execution.input_file(params.get("comp2_cpp"))
        ])
    if params.get("comp2_def") is not None:
        cargs.append(execution.input_file(params.get("comp2_def")))
    if params.get("comp2_output") is not None:
        cargs.append(params.get("comp2_output"))
    if params.get("comp3_def2") is not None:
        cargs.extend([
            "-comp3",
            execution.input_file(params.get("comp3_def2"))
        ])
    if params.get("comp3_def1") is not None:
        cargs.append(execution.input_file(params.get("comp3_def1")))
    if params.get("comp3_output") is not None:
        cargs.append(params.get("comp3_output"))
    if params.get("def2disp_input") is not None:
        cargs.extend([
            "-def2disp",
            execution.input_file(params.get("def2disp_input"))
        ])
    if params.get("def2disp_output") is not None:
        cargs.append(params.get("def2disp_output"))
    if params.get("disp2def_input") is not None:
        cargs.extend([
            "-disp2def",
            execution.input_file(params.get("disp2def_input"))
        ])
    if params.get("disp2def_output") is not None:
        cargs.append(params.get("disp2def_output"))
    if params.get("upd_sform_image") is not None:
        cargs.extend([
            "-updSform",
            execution.input_file(params.get("upd_sform_image"))
        ])
    if params.get("upd_sform_affine") is not None:
        cargs.append(execution.input_file(params.get("upd_sform_affine")))
    if params.get("upd_sform_output") is not None:
        cargs.append(params.get("upd_sform_output"))
    if params.get("aff2def_affine") is not None:
        cargs.extend([
            "-aff2def",
            execution.input_file(params.get("aff2def_affine"))
        ])
    if params.get("aff2def_target") is not None:
        cargs.append(execution.input_file(params.get("aff2def_target")))
    if params.get("aff2def_cpp_or_def") is not None:
        cargs.append(execution.input_file(params.get("aff2def_cpp_or_def")))
    if params.get("aff2def_output") is not None:
        cargs.append(params.get("aff2def_output"))
    if params.get("inv_affine_input") is not None:
        cargs.extend([
            "-invAffine",
            execution.input_file(params.get("inv_affine_input"))
        ])
    if params.get("inv_affine_output") is not None:
        cargs.append(params.get("inv_affine_output"))
    if params.get("comp_aff_1st") is not None:
        cargs.extend([
            "-compAff",
            execution.input_file(params.get("comp_aff_1st"))
        ])
    if params.get("comp_aff_2nd") is not None:
        cargs.append(execution.input_file(params.get("comp_aff_2nd")))
    if params.get("comp_aff_output") is not None:
        cargs.append(params.get("comp_aff_output"))
    return cargs


def reg_transform_outputs(
    params: RegTransformParameters,
    execution: Execution,
) -> RegTransformOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RegTransformOutputs(
        root=execution.output_file("."),
        cpp2def_output_file=execution.output_file(params.get("cpp2def_output")) if (params.get("cpp2def_output") is not None) else None,
        comp1_output_file=execution.output_file(params.get("comp1_output")) if (params.get("comp1_output") is not None) else None,
        comp2_output_file=execution.output_file(params.get("comp2_output")) if (params.get("comp2_output") is not None) else None,
        comp3_output_file=execution.output_file(params.get("comp3_output")) if (params.get("comp3_output") is not None) else None,
        def2disp_output_file=execution.output_file(params.get("def2disp_output")) if (params.get("def2disp_output") is not None) else None,
        disp2def_output_file=execution.output_file(params.get("disp2def_output")) if (params.get("disp2def_output") is not None) else None,
        upd_sform_output_file=execution.output_file(params.get("upd_sform_output")) if (params.get("upd_sform_output") is not None) else None,
        aff2def_output_file=execution.output_file(params.get("aff2def_output")) if (params.get("aff2def_output") is not None) else None,
        inv_affine_output_file=execution.output_file(params.get("inv_affine_output")) if (params.get("inv_affine_output") is not None) else None,
        comp_aff_output_file=execution.output_file(params.get("comp_aff_output")) if (params.get("comp_aff_output") is not None) else None,
    )
    return ret


def reg_transform_execute(
    params: RegTransformParameters,
    execution: Execution,
) -> RegTransformOutputs:
    """
    Tool for performing various transformation operations on medical images
    including control point to deformation conversion, composition of
    transformations, and converting between deformation and displacement fields.
    
    Author: NiftyReg Developers
    
    URL: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RegTransformOutputs`).
    """
    params = execution.params(params)
    cargs = reg_transform_cargs(params, execution)
    ret = reg_transform_outputs(params, execution)
    execution.run(cargs)
    return ret


def reg_transform(
    reference_image: InputPathType,
    cpp2def_input: InputPathType | None = None,
    cpp2def_output: str | None = None,
    comp1_cpp2: InputPathType | None = None,
    comp1_cpp1: InputPathType | None = None,
    comp1_output: str | None = None,
    comp2_cpp: InputPathType | None = None,
    comp2_def: InputPathType | None = None,
    comp2_output: str | None = None,
    comp3_def2: InputPathType | None = None,
    comp3_def1: InputPathType | None = None,
    comp3_output: str | None = None,
    def2disp_input: InputPathType | None = None,
    def2disp_output: str | None = None,
    disp2def_input: InputPathType | None = None,
    disp2def_output: str | None = None,
    upd_sform_image: InputPathType | None = None,
    upd_sform_affine: InputPathType | None = None,
    upd_sform_output: str | None = None,
    aff2def_affine: InputPathType | None = None,
    aff2def_target: InputPathType | None = None,
    aff2def_cpp_or_def: InputPathType | None = None,
    aff2def_output: str | None = None,
    inv_affine_input: InputPathType | None = None,
    inv_affine_output: str | None = None,
    comp_aff_1st: InputPathType | None = None,
    comp_aff_2nd: InputPathType | None = None,
    comp_aff_output: str | None = None,
    runner: Runner | None = None,
) -> RegTransformOutputs:
    """
    Tool for performing various transformation operations on medical images
    including control point to deformation conversion, composition of
    transformations, and converting between deformation and displacement fields.
    
    Author: NiftyReg Developers
    
    URL: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        reference_image: Filename of the reference image.
        cpp2def_input: Conversion from control point position to deformation\
            field. Filename of input lattice of control point positions (CPP).
        cpp2def_output: Filename of the output deformation field image (DEF).
        comp1_cpp2: Composition of two lattices of control points.\
            CPP2(CPP1(x)). Filename of lattice of control point that contains the\
            second deformation (CPP2).
        comp1_cpp1: Filename of lattice of control point that contains the\
            initial deformation (CPP1).
        comp1_output: Filename of the output deformation field.
        comp2_cpp: Composition of a deformation field with a lattice of control\
            points. CPP(DEF(x)). Filename of lattice of control point that contains\
            the second deformation (CPP).
        comp2_def: Filename of the deformation field to be used as initial\
            deformation (DEF).
        comp2_output: Filename of the output deformation field.
        comp3_def2: Composition of two deformation fields. DEF2(DEF1(x)).\
            Filename of the second deformation field (DEF2).
        comp3_def1: Filename of the first deformation field (DEF1).
        comp3_output: Filename of the output deformation field.
        def2disp_input: Convert a deformation field into a displacement field.\
            Filename of deformation field x'=T(x).
        def2disp_output: Filename of displacement field x'=x+T(x).
        disp2def_input: Convert a displacement field into a deformation field.\
            Filename of displacement field x'=x+T(x).
        disp2def_output: Filename of deformation field x'=T(x).
        upd_sform_image: Update the sform of a floating (source) image using an\
            affine transformation. Filename of image to be updated.
        upd_sform_affine: Affine transformation defined as Affine x Reference =\
            Floating. Filename of affine transformation.
        upd_sform_output: Updated image filename.
        aff2def_affine: Compose a non-rigid with an affine. Filename of affine\
            transformation.
        aff2def_target: Image used as a target for the non-rigid step.
        aff2def_cpp_or_def: Reference image (B). Filename of control point\
            position or deformation field.
        aff2def_output: Output deformation field filename.
        inv_affine_input: Invert an affine transformation matrix. Filename of\
            input affine matrix.
        inv_affine_output: Filename of inverted affine matrix.
        comp_aff_1st: Compose two affine transformation matrices. Filename of\
            first affine matrix.
        comp_aff_2nd: Filename of second affine matrix.
        comp_aff_output: Filename of composed affine matrix result.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegTransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_TRANSFORM_METADATA)
    params = reg_transform_params(
        reference_image=reference_image,
        cpp2def_input=cpp2def_input,
        cpp2def_output=cpp2def_output,
        comp1_cpp2=comp1_cpp2,
        comp1_cpp1=comp1_cpp1,
        comp1_output=comp1_output,
        comp2_cpp=comp2_cpp,
        comp2_def=comp2_def,
        comp2_output=comp2_output,
        comp3_def2=comp3_def2,
        comp3_def1=comp3_def1,
        comp3_output=comp3_output,
        def2disp_input=def2disp_input,
        def2disp_output=def2disp_output,
        disp2def_input=disp2def_input,
        disp2def_output=disp2def_output,
        upd_sform_image=upd_sform_image,
        upd_sform_affine=upd_sform_affine,
        upd_sform_output=upd_sform_output,
        aff2def_affine=aff2def_affine,
        aff2def_target=aff2def_target,
        aff2def_cpp_or_def=aff2def_cpp_or_def,
        aff2def_output=aff2def_output,
        inv_affine_input=inv_affine_input,
        inv_affine_output=inv_affine_output,
        comp_aff_1st=comp_aff_1st,
        comp_aff_2nd=comp_aff_2nd,
        comp_aff_output=comp_aff_output,
    )
    return reg_transform_execute(params, execution)


__all__ = [
    "REG_TRANSFORM_METADATA",
    "RegTransformOutputs",
    "RegTransformParameters",
    "reg_transform",
    "reg_transform_params",
]
