# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ALLINEATE_METADATA = Metadata(
    id="05acda1bcc694397c89e84c0f214f9da9cbb22ef.boutiques",
    name="3dAllineate",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dAllineateParameters = typing.TypedDict('V3dAllineateParameters', {
    "__STYX_TYPE__": typing.Literal["3dAllineate"],
    "source": InputPathType,
    "base": typing.NotRequired[InputPathType | None],
    "prefix": str,
    "param_save": typing.NotRequired[str | None],
    "param_apply": typing.NotRequired[str | None],
    "matrix_save": typing.NotRequired[str | None],
    "matrix_apply": typing.NotRequired[str | None],
    "cost": typing.NotRequired[str | None],
    "interp": typing.NotRequired[str | None],
    "final": typing.NotRequired[str | None],
    "nmatch": typing.NotRequired[float | None],
    "nopad": bool,
    "verbose": bool,
    "quiet": bool,
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
        "3dAllineate": v_3d_allineate_cargs,
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
        "3dAllineate": v_3d_allineate_outputs,
    }.get(t)


class V3dAllineateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_allineate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_brik: OutputPathType
    """Output dataset brick file"""
    out_head: OutputPathType
    """Output dataset head file"""
    out_param_save: OutputPathType | None
    """File holding saved warp parameters"""
    out_matrix_save: OutputPathType | None
    """File holding saved matrix transformations"""


def v_3d_allineate_params(
    source: InputPathType,
    prefix: str,
    base: InputPathType | None = None,
    param_save: str | None = None,
    param_apply: str | None = None,
    matrix_save: str | None = None,
    matrix_apply: str | None = None,
    cost: str | None = None,
    interp: str | None = None,
    final: str | None = None,
    nmatch: float | None = None,
    nopad: bool = False,
    verbose: bool = False,
    quiet: bool = False,
) -> V3dAllineateParameters:
    """
    Build parameters.
    
    Args:
        source: Source dataset file.
        prefix: Output prefix.
        base: Base dataset file.
        param_save: Save the warp parameters in ASCII (.1D) format into file.
        param_apply: Read warp parameters from file and apply them to the\
            source dataset.
        matrix_save: Save the transformation matrix for each sub-brick into\
            file.
        matrix_apply: Use the matrices in file to define the spatial\
            transformations to be applied.
        cost: Defines the 'cost' function that defines the matching between the\
            source and the base.
        interp: Defines interpolation method to use during matching process.
        final: Defines the interpolation mode used to create the output dataset.
        nmatch: Use at most 'nnn' scattered points to match the datasets.
        nopad: Do not use zero-padding on the base image.
        verbose: Print out verbose progress reports.
        quiet: Don't print out verbose stuff.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dAllineate",
        "source": source,
        "prefix": prefix,
        "nopad": nopad,
        "verbose": verbose,
        "quiet": quiet,
    }
    if base is not None:
        params["base"] = base
    if param_save is not None:
        params["param_save"] = param_save
    if param_apply is not None:
        params["param_apply"] = param_apply
    if matrix_save is not None:
        params["matrix_save"] = matrix_save
    if matrix_apply is not None:
        params["matrix_apply"] = matrix_apply
    if cost is not None:
        params["cost"] = cost
    if interp is not None:
        params["interp"] = interp
    if final is not None:
        params["final"] = final
    if nmatch is not None:
        params["nmatch"] = nmatch
    return params


def v_3d_allineate_cargs(
    params: V3dAllineateParameters,
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
    cargs.append("3dAllineate")
    cargs.append(execution.input_file(params.get("source")))
    if params.get("base") is not None:
        cargs.extend([
            "-base",
            execution.input_file(params.get("base"))
        ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("param_save") is not None:
        cargs.extend([
            "-1Dparam_save",
            params.get("param_save")
        ])
    if params.get("param_apply") is not None:
        cargs.extend([
            "-1Dparam_apply",
            params.get("param_apply")
        ])
    if params.get("matrix_save") is not None:
        cargs.extend([
            "-1Dmatrix_save",
            params.get("matrix_save")
        ])
    if params.get("matrix_apply") is not None:
        cargs.extend([
            "-1Dmatrix_apply",
            params.get("matrix_apply")
        ])
    if params.get("cost") is not None:
        cargs.extend([
            "-cost",
            params.get("cost")
        ])
    if params.get("interp") is not None:
        cargs.extend([
            "-interp",
            params.get("interp")
        ])
    if params.get("final") is not None:
        cargs.extend([
            "-final",
            params.get("final")
        ])
    if params.get("nmatch") is not None:
        cargs.extend([
            "-nmatch",
            str(params.get("nmatch"))
        ])
    if params.get("nopad"):
        cargs.append("-nopad")
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("quiet"):
        cargs.append("-quiet")
    return cargs


def v_3d_allineate_outputs(
    params: V3dAllineateParameters,
    execution: Execution,
) -> V3dAllineateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dAllineateOutputs(
        root=execution.output_file("."),
        out_brik=execution.output_file(params.get("prefix") + "+orig.BRIK"),
        out_head=execution.output_file(params.get("prefix") + "+orig.HEAD"),
        out_param_save=execution.output_file(params.get("param_save")) if (params.get("param_save") is not None) else None,
        out_matrix_save=execution.output_file(params.get("matrix_save")) if (params.get("matrix_save") is not None) else None,
    )
    return ret


def v_3d_allineate_execute(
    params: V3dAllineateParameters,
    execution: Execution,
) -> V3dAllineateOutputs:
    """
    Program to align one dataset (the 'source') to a 'base' dataset using an affine
    (matrix) transformation of space.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dAllineateOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_allineate_cargs(params, execution)
    ret = v_3d_allineate_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_allineate(
    source: InputPathType,
    prefix: str,
    base: InputPathType | None = None,
    param_save: str | None = None,
    param_apply: str | None = None,
    matrix_save: str | None = None,
    matrix_apply: str | None = None,
    cost: str | None = None,
    interp: str | None = None,
    final: str | None = None,
    nmatch: float | None = None,
    nopad: bool = False,
    verbose: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dAllineateOutputs:
    """
    Program to align one dataset (the 'source') to a 'base' dataset using an affine
    (matrix) transformation of space.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        source: Source dataset file.
        prefix: Output prefix.
        base: Base dataset file.
        param_save: Save the warp parameters in ASCII (.1D) format into file.
        param_apply: Read warp parameters from file and apply them to the\
            source dataset.
        matrix_save: Save the transformation matrix for each sub-brick into\
            file.
        matrix_apply: Use the matrices in file to define the spatial\
            transformations to be applied.
        cost: Defines the 'cost' function that defines the matching between the\
            source and the base.
        interp: Defines interpolation method to use during matching process.
        final: Defines the interpolation mode used to create the output dataset.
        nmatch: Use at most 'nnn' scattered points to match the datasets.
        nopad: Do not use zero-padding on the base image.
        verbose: Print out verbose progress reports.
        quiet: Don't print out verbose stuff.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAllineateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ALLINEATE_METADATA)
    params = v_3d_allineate_params(
        source=source,
        base=base,
        prefix=prefix,
        param_save=param_save,
        param_apply=param_apply,
        matrix_save=matrix_save,
        matrix_apply=matrix_apply,
        cost=cost,
        interp=interp,
        final=final,
        nmatch=nmatch,
        nopad=nopad,
        verbose=verbose,
        quiet=quiet,
    )
    return v_3d_allineate_execute(params, execution)


__all__ = [
    "V3dAllineateOutputs",
    "V3dAllineateParameters",
    "V_3D_ALLINEATE_METADATA",
    "v_3d_allineate",
    "v_3d_allineate_params",
]
