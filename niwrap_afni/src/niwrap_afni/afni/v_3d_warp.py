# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_WARP_METADATA = Metadata(
    id="f905d9db7eb4dc5e4bba6d7a453936b46a2e8f24.boutiques",
    name="3dWarp",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dWarpParameters = typing.TypedDict('V3dWarpParameters', {
    "__STYXTYPE__": typing.Literal["3dWarp"],
    "matvec_in2out": typing.NotRequired[InputPathType | None],
    "matvec_out2in": typing.NotRequired[InputPathType | None],
    "tta2mni": bool,
    "mni2tta": bool,
    "matparent": typing.NotRequired[str | None],
    "card2oblique": typing.NotRequired[str | None],
    "oblique_parent": typing.NotRequired[str | None],
    "deoblique": bool,
    "oblique2card": bool,
    "disp_obl_xform_only": bool,
    "linear": bool,
    "cubic": bool,
    "NN": bool,
    "quintic": bool,
    "wsinc5": bool,
    "fsl_matvec": bool,
    "newgrid": typing.NotRequired[float | None],
    "gridset": typing.NotRequired[str | None],
    "zpad": typing.NotRequired[float | None],
    "verb": bool,
    "prefix": typing.NotRequired[str | None],
    "dataset": str,
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
        "3dWarp": v_3d_warp_cargs,
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


class V3dWarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_warp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_warp_params(
    dataset: str,
    matvec_in2out: InputPathType | None = None,
    matvec_out2in: InputPathType | None = None,
    tta2mni: bool = False,
    mni2tta: bool = False,
    matparent: str | None = None,
    card2oblique: str | None = None,
    oblique_parent: str | None = None,
    deoblique: bool = False,
    oblique2card: bool = False,
    disp_obl_xform_only: bool = False,
    linear: bool = False,
    cubic: bool = False,
    nn: bool = False,
    quintic: bool = False,
    wsinc5: bool = False,
    fsl_matvec: bool = False,
    newgrid: float | None = None,
    gridset: str | None = None,
    zpad: float | None = None,
    verb: bool = False,
    prefix: str | None = None,
) -> V3dWarpParameters:
    """
    Build parameters.
    
    Args:
        dataset: Input dataset to be warped.
        matvec_in2out: Read a 3x4 affine transform matrix+vector from file.
        matvec_out2in: Read a 3x4 affine transform matrix+vector from file.
        tta2mni: Transform a dataset in Talairach-Tournoux Atlas coordinates to\
            MNI-152 coordinates.
        mni2tta: Transform a dataset in MNI-152 coordinates to\
            Talairach-Tournoux Atlas coordinates.
        matparent: Read in the matrix from WARPDRIVE_MATVEC_* attributes in the\
            header of dataset.
        card2oblique: Make cardinal dataset oblique to match oblique dataset.
        oblique_parent: Make cardinal dataset oblique to match oblique dataset.
        deoblique: Transform an oblique dataset to a cardinal dataset.
        oblique2card: Transform an oblique dataset to a cardinal dataset.
        disp_obl_xform_only: Display the obliquity transform matrix.
        linear: Use linear interpolation.
        cubic: Use cubic interpolation.
        nn: Use nearest neighbor interpolation.
        quintic: Use quintic interpolation.
        wsinc5: Use wsinc5 interpolation.
        fsl_matvec: Indicates that the matrix file uses FSL ordered coordinates\
            ('LPI').
        newgrid: Compute new dataset on a new 3D grid, with specified spacing.
        gridset: Compute new dataset on the same grid as another dataset.
        zpad: Pad input dataset with specified planes of zeros on all sides\
            before transformation.
        verb: Print out some information along the way.
        prefix: Set the prefix of the output dataset.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dWarp",
        "tta2mni": tta2mni,
        "mni2tta": mni2tta,
        "deoblique": deoblique,
        "oblique2card": oblique2card,
        "disp_obl_xform_only": disp_obl_xform_only,
        "linear": linear,
        "cubic": cubic,
        "NN": nn,
        "quintic": quintic,
        "wsinc5": wsinc5,
        "fsl_matvec": fsl_matvec,
        "verb": verb,
        "dataset": dataset,
    }
    if matvec_in2out is not None:
        params["matvec_in2out"] = matvec_in2out
    if matvec_out2in is not None:
        params["matvec_out2in"] = matvec_out2in
    if matparent is not None:
        params["matparent"] = matparent
    if card2oblique is not None:
        params["card2oblique"] = card2oblique
    if oblique_parent is not None:
        params["oblique_parent"] = oblique_parent
    if newgrid is not None:
        params["newgrid"] = newgrid
    if gridset is not None:
        params["gridset"] = gridset
    if zpad is not None:
        params["zpad"] = zpad
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_warp_cargs(
    params: V3dWarpParameters,
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
    cargs.append("3dWarp")
    if params.get("matvec_in2out") is not None:
        cargs.extend([
            "-matvec_in2out",
            execution.input_file(params.get("matvec_in2out"))
        ])
    if params.get("matvec_out2in") is not None:
        cargs.extend([
            "-matvec_out2in",
            execution.input_file(params.get("matvec_out2in"))
        ])
    if params.get("tta2mni"):
        cargs.append("-tta2mni")
    if params.get("mni2tta"):
        cargs.append("-mni2tta")
    if params.get("matparent") is not None:
        cargs.extend([
            "-matparent",
            params.get("matparent")
        ])
    if params.get("card2oblique") is not None:
        cargs.extend([
            "-card2oblique",
            params.get("card2oblique")
        ])
    if params.get("oblique_parent") is not None:
        cargs.extend([
            "-oblique_parent",
            params.get("oblique_parent")
        ])
    if params.get("deoblique"):
        cargs.append("-deoblique")
    if params.get("oblique2card"):
        cargs.append("-oblique2card")
    if params.get("disp_obl_xform_only"):
        cargs.append("-disp_obl_xform_only")
    if params.get("linear"):
        cargs.append("-linear")
    if params.get("cubic"):
        cargs.append("-cubic")
    if params.get("NN"):
        cargs.append("-NN")
    if params.get("quintic"):
        cargs.append("-quintic")
    if params.get("wsinc5"):
        cargs.append("-wsinc5")
    if params.get("fsl_matvec"):
        cargs.append("-fsl_matvec")
    if params.get("newgrid") is not None:
        cargs.extend([
            "-newgrid",
            str(params.get("newgrid"))
        ])
    if params.get("gridset") is not None:
        cargs.extend([
            "-gridset",
            params.get("gridset")
        ])
    if params.get("zpad") is not None:
        cargs.extend([
            "-zpad",
            str(params.get("zpad"))
        ])
    if params.get("verb"):
        cargs.append("-verb")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    cargs.append(params.get("dataset"))
    return cargs


def v_3d_warp_outputs(
    params: V3dWarpParameters,
    execution: Execution,
) -> V3dWarpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dWarpOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3d_warp_execute(
    params: V3dWarpParameters,
    execution: Execution,
) -> V3dWarpOutputs:
    """
    Warp (spatially transform) one 3D dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dWarpOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_warp_cargs(params, execution)
    ret = v_3d_warp_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_warp(
    dataset: str,
    matvec_in2out: InputPathType | None = None,
    matvec_out2in: InputPathType | None = None,
    tta2mni: bool = False,
    mni2tta: bool = False,
    matparent: str | None = None,
    card2oblique: str | None = None,
    oblique_parent: str | None = None,
    deoblique: bool = False,
    oblique2card: bool = False,
    disp_obl_xform_only: bool = False,
    linear: bool = False,
    cubic: bool = False,
    nn: bool = False,
    quintic: bool = False,
    wsinc5: bool = False,
    fsl_matvec: bool = False,
    newgrid: float | None = None,
    gridset: str | None = None,
    zpad: float | None = None,
    verb: bool = False,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dWarpOutputs:
    """
    Warp (spatially transform) one 3D dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input dataset to be warped.
        matvec_in2out: Read a 3x4 affine transform matrix+vector from file.
        matvec_out2in: Read a 3x4 affine transform matrix+vector from file.
        tta2mni: Transform a dataset in Talairach-Tournoux Atlas coordinates to\
            MNI-152 coordinates.
        mni2tta: Transform a dataset in MNI-152 coordinates to\
            Talairach-Tournoux Atlas coordinates.
        matparent: Read in the matrix from WARPDRIVE_MATVEC_* attributes in the\
            header of dataset.
        card2oblique: Make cardinal dataset oblique to match oblique dataset.
        oblique_parent: Make cardinal dataset oblique to match oblique dataset.
        deoblique: Transform an oblique dataset to a cardinal dataset.
        oblique2card: Transform an oblique dataset to a cardinal dataset.
        disp_obl_xform_only: Display the obliquity transform matrix.
        linear: Use linear interpolation.
        cubic: Use cubic interpolation.
        nn: Use nearest neighbor interpolation.
        quintic: Use quintic interpolation.
        wsinc5: Use wsinc5 interpolation.
        fsl_matvec: Indicates that the matrix file uses FSL ordered coordinates\
            ('LPI').
        newgrid: Compute new dataset on a new 3D grid, with specified spacing.
        gridset: Compute new dataset on the same grid as another dataset.
        zpad: Pad input dataset with specified planes of zeros on all sides\
            before transformation.
        verb: Print out some information along the way.
        prefix: Set the prefix of the output dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dWarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_WARP_METADATA)
    params = v_3d_warp_params(
        matvec_in2out=matvec_in2out,
        matvec_out2in=matvec_out2in,
        tta2mni=tta2mni,
        mni2tta=mni2tta,
        matparent=matparent,
        card2oblique=card2oblique,
        oblique_parent=oblique_parent,
        deoblique=deoblique,
        oblique2card=oblique2card,
        disp_obl_xform_only=disp_obl_xform_only,
        linear=linear,
        cubic=cubic,
        nn=nn,
        quintic=quintic,
        wsinc5=wsinc5,
        fsl_matvec=fsl_matvec,
        newgrid=newgrid,
        gridset=gridset,
        zpad=zpad,
        verb=verb,
        prefix=prefix,
        dataset=dataset,
    )
    return v_3d_warp_execute(params, execution)


__all__ = [
    "V3dWarpOutputs",
    "V3dWarpParameters",
    "V_3D_WARP_METADATA",
    "v_3d_warp",
    "v_3d_warp_params",
]
