# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_TAGALIGN_METADATA = Metadata(
    id="475b53c4b6432ecad79b017ae32826c765d7c00c.boutiques",
    name="3dTagalign",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dTagalignParameters = typing.TypedDict('V3dTagalignParameters', {
    "__STYXTYPE__": typing.Literal["3dTagalign"],
    "input_dataset": InputPathType,
    "master_dataset": InputPathType,
    "tagset_file": typing.NotRequired[InputPathType | None],
    "no_keep_tags": bool,
    "matvec_file": typing.NotRequired[str | None],
    "rotate": bool,
    "affine": bool,
    "rotscl": bool,
    "prefix": typing.NotRequired[str | None],
    "verbose": bool,
    "dummy": bool,
    "linear_interpolation": bool,
    "cubic_interpolation": bool,
    "nearest_neighbor_interpolation": bool,
    "quintic_interpolation": bool,
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
        "3dTagalign": v_3d_tagalign_cargs,
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
        "3dTagalign": v_3d_tagalign_outputs,
    }.get(t)


class V3dTagalignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tagalign(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset_head: OutputPathType | None
    """Output dataset in AFNI format (.HEAD)"""
    output_dataset_brick: OutputPathType | None
    """Output dataset in AFNI format (.BRIK)"""
    output_matvec_file: OutputPathType | None
    """Output transformation matrix and vector file"""


def v_3d_tagalign_params(
    input_dataset: InputPathType,
    master_dataset: InputPathType,
    tagset_file: InputPathType | None = None,
    no_keep_tags: bool = False,
    matvec_file: str | None = None,
    rotate: bool = False,
    affine: bool = False,
    rotscl: bool = False,
    prefix: str | None = None,
    verbose: bool = False,
    dummy: bool = False,
    linear_interpolation: bool = False,
    cubic_interpolation: bool = False,
    nearest_neighbor_interpolation: bool = False,
    quintic_interpolation: bool = False,
) -> V3dTagalignParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset to align.
        master_dataset: Use dataset 'mset' as the master dataset. This option\
            is mandatory.
        tagset_file: Use the tagset in the .tag file instead of dset.
        no_keep_tags: Don't put transformed locations of dset's tags into the\
            output dataset [default = keep tags].
        matvec_file: Write the matrix+vector transformation to file 'mfile'.\
            This can be used with 3dWarp's '-matvec_in2out' option to align other\
            datasets in the same way (e.g., functional datasets).
        rotate: Compute the transformation as a rotation + shift (default).
        affine: Compute the transformation as a general affine map, where the\
            matrix is a general 3x3 matrix.
        rotscl: Compute transformation as a rotation times an isotropic\
            scaling; where matrix is an orthogonal matrix times a scalar.
        prefix: Specify the prefix for the output dataset.
        verbose: Print progress reports.
        dummy: Don't actually rotate the dataset, just compute the\
            transformation matrix and vector. If '-matvec' is used, the mfile will\
            be written.
        linear_interpolation: Use linear interpolation method.
        cubic_interpolation: Use cubic interpolation method (default).
        nearest_neighbor_interpolation: Use nearest neighbour interpolation\
            method.
        quintic_interpolation: Use quintic interpolation method.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dTagalign",
        "input_dataset": input_dataset,
        "master_dataset": master_dataset,
        "no_keep_tags": no_keep_tags,
        "rotate": rotate,
        "affine": affine,
        "rotscl": rotscl,
        "verbose": verbose,
        "dummy": dummy,
        "linear_interpolation": linear_interpolation,
        "cubic_interpolation": cubic_interpolation,
        "nearest_neighbor_interpolation": nearest_neighbor_interpolation,
        "quintic_interpolation": quintic_interpolation,
    }
    if tagset_file is not None:
        params["tagset_file"] = tagset_file
    if matvec_file is not None:
        params["matvec_file"] = matvec_file
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_tagalign_cargs(
    params: V3dTagalignParameters,
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
    cargs.append("3dTagalign")
    cargs.append(execution.input_file(params.get("input_dataset")))
    cargs.extend([
        "-master",
        execution.input_file(params.get("master_dataset"))
    ])
    if params.get("tagset_file") is not None:
        cargs.extend([
            "-tagset",
            execution.input_file(params.get("tagset_file"))
        ])
    if params.get("no_keep_tags"):
        cargs.append("-nokeeptags")
    if params.get("matvec_file") is not None:
        cargs.extend([
            "-matvec",
            params.get("matvec_file")
        ])
    if params.get("rotate"):
        cargs.append("-rotate")
    if params.get("affine"):
        cargs.append("-affine")
    if params.get("rotscl"):
        cargs.append("-rotscl")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("dummy"):
        cargs.append("-dummy")
    if params.get("linear_interpolation"):
        cargs.append("-linear")
    if params.get("cubic_interpolation"):
        cargs.append("-cubic")
    if params.get("nearest_neighbor_interpolation"):
        cargs.append("-NN")
    if params.get("quintic_interpolation"):
        cargs.append("-quintic")
    return cargs


def v_3d_tagalign_outputs(
    params: V3dTagalignParameters,
    execution: Execution,
) -> V3dTagalignOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dTagalignOutputs(
        root=execution.output_file("."),
        output_dataset_head=execution.output_file(params.get("prefix") + "+orig.HEAD") if (params.get("prefix") is not None) else None,
        output_dataset_brick=execution.output_file(params.get("prefix") + "+orig.BRIK") if (params.get("prefix") is not None) else None,
        output_matvec_file=execution.output_file(params.get("matvec_file")) if (params.get("matvec_file") is not None) else None,
    )
    return ret


def v_3d_tagalign_execute(
    params: V3dTagalignParameters,
    execution: Execution,
) -> V3dTagalignOutputs:
    """
    Rotates/translates dataset 'dset' to be aligned with the master using the
    tagsets embedded in their .HEAD files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dTagalignOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_tagalign_cargs(params, execution)
    ret = v_3d_tagalign_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_tagalign(
    input_dataset: InputPathType,
    master_dataset: InputPathType,
    tagset_file: InputPathType | None = None,
    no_keep_tags: bool = False,
    matvec_file: str | None = None,
    rotate: bool = False,
    affine: bool = False,
    rotscl: bool = False,
    prefix: str | None = None,
    verbose: bool = False,
    dummy: bool = False,
    linear_interpolation: bool = False,
    cubic_interpolation: bool = False,
    nearest_neighbor_interpolation: bool = False,
    quintic_interpolation: bool = False,
    runner: Runner | None = None,
) -> V3dTagalignOutputs:
    """
    Rotates/translates dataset 'dset' to be aligned with the master using the
    tagsets embedded in their .HEAD files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset to align.
        master_dataset: Use dataset 'mset' as the master dataset. This option\
            is mandatory.
        tagset_file: Use the tagset in the .tag file instead of dset.
        no_keep_tags: Don't put transformed locations of dset's tags into the\
            output dataset [default = keep tags].
        matvec_file: Write the matrix+vector transformation to file 'mfile'.\
            This can be used with 3dWarp's '-matvec_in2out' option to align other\
            datasets in the same way (e.g., functional datasets).
        rotate: Compute the transformation as a rotation + shift (default).
        affine: Compute the transformation as a general affine map, where the\
            matrix is a general 3x3 matrix.
        rotscl: Compute transformation as a rotation times an isotropic\
            scaling; where matrix is an orthogonal matrix times a scalar.
        prefix: Specify the prefix for the output dataset.
        verbose: Print progress reports.
        dummy: Don't actually rotate the dataset, just compute the\
            transformation matrix and vector. If '-matvec' is used, the mfile will\
            be written.
        linear_interpolation: Use linear interpolation method.
        cubic_interpolation: Use cubic interpolation method (default).
        nearest_neighbor_interpolation: Use nearest neighbour interpolation\
            method.
        quintic_interpolation: Use quintic interpolation method.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTagalignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TAGALIGN_METADATA)
    params = v_3d_tagalign_params(
        input_dataset=input_dataset,
        master_dataset=master_dataset,
        tagset_file=tagset_file,
        no_keep_tags=no_keep_tags,
        matvec_file=matvec_file,
        rotate=rotate,
        affine=affine,
        rotscl=rotscl,
        prefix=prefix,
        verbose=verbose,
        dummy=dummy,
        linear_interpolation=linear_interpolation,
        cubic_interpolation=cubic_interpolation,
        nearest_neighbor_interpolation=nearest_neighbor_interpolation,
        quintic_interpolation=quintic_interpolation,
    )
    return v_3d_tagalign_execute(params, execution)


__all__ = [
    "V3dTagalignOutputs",
    "V3dTagalignParameters",
    "V_3D_TAGALIGN_METADATA",
    "v_3d_tagalign",
    "v_3d_tagalign_params",
]
